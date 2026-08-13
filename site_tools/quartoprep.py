from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import threading
import time
import urllib.request
from pathlib import Path

import pathspec
import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "self"
STAGE = ROOT / "quarto_src"
SITE = ROOT / "site"
CONFIG = ROOT / "_quarto.yml"
SITEIGNORE = ROOT / ".siteignore"
VENDOR = ROOT / "site_tools" / "vendor"

SITE_URL = "https://britoalv.github.io/directedArticles/"
DEPLOY_ENV = "QUARTO_DEPLOY"

CODE_OUTPUT_DIR = "codeview"

CODE_EXTENSIONS = {
    ".rs", ".py", ".toml", ".sh", ".bash", ".js", ".ts", ".jsx", ".tsx",
    ".json", ".yml", ".yaml", ".c", ".h", ".cpp", ".hpp", ".java", ".go",
    ".rb", ".txt", ".ini", ".cfg", ".sql", ".html", ".css", ".lock",
}

LANGS = {
    ".rs": "rust", ".py": "python", ".toml": "toml", ".sh": "bash",
    ".bash": "bash", ".js": "javascript", ".ts": "typescript",
    ".jsx": "jsx", ".tsx": "tsx", ".json": "json", ".yml": "yaml",
    ".yaml": "yaml", ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp",
    ".java": "java", ".go": "go", ".rb": "ruby", ".txt": "text",
    ".ini": "ini", ".cfg": "ini", ".sql": "sql", ".html": "html",
    ".css": "css",
}

KATEX_CDN_RE = re.compile(
    r"https://cdn\.jsdelivr\.net/npm/katex@[A-Za-z0-9.]+/dist/(katex\.min\.(?:js|css))"
)
POLYFILL_RE = re.compile(
    r'\s*<script[^>]*src="https://cdnjs\.cloudflare\.com/polyfill[^"]*"[^>]*></script>\s*'
)
CDN_RE = re.compile(
    r"(https?://(?:cdn\.jsdelivr\.net|cdn\.quarto\.org|cdnjs\.cloudflare\.com|"
    r"fonts\.googleapis\.com|fonts\.gstatic\.com)[^\s\"'<>]*)"
)

MD_LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)\s]+)\)")
HREF_RE = re.compile(r'(<a\s[^>]*?href=")([^"]*)(")')


def load_specs(deploy: bool) -> list[tuple[str, pathspec.GitIgnoreSpec]]:
    specs: list[tuple[str, pathspec.GitIgnoreSpec]] = []

    def add(path: Path, base: str) -> None:
        if not path.is_file():
            return
        lines = path.read_text(encoding="utf-8").splitlines()
        if lines:
            specs.append((base, pathspec.GitIgnoreSpec.from_lines(lines)))

    add(ROOT / ".gitignore", "")
    for ignore in SRC.rglob(".gitignore"):
        base = ignore.parent.relative_to(ROOT).as_posix()
        add(ignore, base)
    if deploy:
        add(SITEIGNORE, "")
    return specs


def is_ignored(rel_from_root: str, specs: list[tuple[str, pathspec.GitIgnoreSpec]]) -> bool:
    for base, spec in specs:
        if base:
            if rel_from_root != base and not rel_from_root.startswith(f"{base}/"):
                continue
            local = rel_from_root[len(base):].lstrip("/")
        else:
            local = rel_from_root
        if spec.match_file(local):
            return True
    return False


def write_if_changed(dst: Path, content: str) -> None:
    if dst.is_file() and dst.read_text(encoding="utf-8") == content:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content, encoding="utf-8")


KATEX_VERSION = "0.18.4"
KATEX_TARBALL = f"https://registry.npmjs.org/katex/-/katex-{KATEX_VERSION}.tgz"
KATEX_CACHE = VENDOR / "katex"

ICON_CACHE = VENDOR / "icons"
ICON_BASE = (
    "https://cdn.jsdelivr.net/gh/vscode-icons/vscode-icons@master/icons/"
)

EXT_ICONS = {
    ".rs": "file_type_rust",
    ".py": "file_type_python",
    ".toml": "file_type_toml",
    ".sh": "file_type_shell",
    ".bash": "file_type_shell",
    ".js": "file_type_js",
    ".ts": "file_type_typescript",
    ".jsx": "file_type_reactjs",
    ".tsx": "file_type_reactts",
    ".json": "file_type_json",
    ".yml": "file_type_yaml",
    ".yaml": "file_type_yaml",
    ".c": "file_type_c",
    ".h": "file_type_cheader",
    ".cpp": "file_type_cpp",
    ".hpp": "file_type_cppheader",
    ".java": "file_type_java",
    ".go": "file_type_go",
    ".rb": "file_type_ruby",
    ".txt": "file_type_text",
    ".ini": "file_type_ini",
    ".cfg": "file_type_ini",
    ".sql": "file_type_sql",
    ".html": "file_type_html",
    ".css": "file_type_css",
    ".md": "file_type_markdown",
    ".ipynb": "file_type_jupyter",
}
LOCK_ICONS = {"Cargo.lock": "file_type_cargo", "uv.lock": "file_type_uv"}
DEFAULT_ICON = "default_file"

FONTS_CACHE = VENDOR / "fonts"
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400"
    "&display=swap"
)
GOOGLE_FONTS_RE = re.compile(r'https://fonts\.googleapis\.com/css2\?[^"\'<>]+')
GSTATIC_RE = re.compile(r"url\((https://fonts\.gstatic\.com/[^)]+)\)")


def ensure_katex() -> Path:
    """Return a directory with the pinned KaTeX assets, downloading and caching if needed."""
    fonts = KATEX_CACHE / "fonts"
    if (
        (KATEX_CACHE / "katex.min.js").is_file()
        and (KATEX_CACHE / "katex.min.css").is_file()
        and fonts.is_dir()
        and len(list(fonts.glob("*.woff2"))) >= 10
    ):
        return KATEX_CACHE
    tmp = KATEX_CACHE.with_suffix(".tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    try:
        with urllib.request.urlopen(KATEX_TARBALL, timeout=120) as resp:
            data = resp.read()
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            for member in tar.getmembers():
                if not member.name.startswith("package/dist/"):
                    continue
                rel = member.name[len("package/dist/"):]
                if rel in ("katex.min.js", "katex.min.css") or rel.startswith("fonts/"):
                    member.name = rel
                    tar.extract(member, tmp, filter="data")
    except Exception as exc:
        shutil.rmtree(tmp, ignore_errors=True)
        sys.exit(
            f"KaTeX assets are not cached in {KATEX_CACHE} and fetching {KATEX_TARBALL} "
            f"failed: {exc}"
        )
    shutil.rmtree(KATEX_CACHE, ignore_errors=True)
    os.replace(tmp, KATEX_CACHE)
    print(f"fetched KaTeX {KATEX_VERSION} into {KATEX_CACHE}")
    return KATEX_CACHE


def ensure_fonts() -> Path:
    """Return a directory with Lato woff2 + a local @font-face stylesheet, cached on disk."""
    if (FONTS_CACHE / "lato.css").is_file() and any(
        (FONTS_CACHE / "lato").glob("*.woff2")
    ):
        return FONTS_CACHE
    tmp = FONTS_CACHE.with_suffix(".tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    (tmp / "lato").mkdir(parents=True)

    def fetch(url: str) -> bytes:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
                )
            },
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.read()

    try:
        css = fetch(GOOGLE_FONTS_URL).decode()
    except Exception as exc:
        shutil.rmtree(tmp, ignore_errors=True)
        sys.exit(f"Lato fonts are not cached in {FONTS_CACHE} and fetching {GOOGLE_FONTS_URL} failed: {exc}")

    def localize(match: re.Match) -> str:
        url = match.group(1)
        name = url.rsplit("/", 1)[-1].split("?")[0]
        dest = tmp / "lato" / name
        if not dest.is_file():
            try:
                dest.write_bytes(fetch(url))
            except Exception as exc:
                shutil.rmtree(tmp, ignore_errors=True)
                sys.exit(f"failed to fetch font {url}: {exc}")
        return f"lato/{name}"

    css = GSTATIC_RE.sub(lambda m: f"url({localize(m)})", css)
    (tmp / "lato.css").write_text(css)
    shutil.rmtree(FONTS_CACHE, ignore_errors=True)
    os.replace(tmp, FONTS_CACHE)
    print(f"fetched Lato fonts into {FONTS_CACHE}")
    return FONTS_CACHE


def ensure_file_icons(names: set[str]) -> Path:
    """Return the cache dir with per-extension SVGs, fetching missing ones from
    the vscode-icons set (cached on disk; failed fetches fall back to the
    generic file icon)."""
    ICON_CACHE.mkdir(parents=True, exist_ok=True)
    wanted = names | {DEFAULT_ICON}
    fetched = {p.name.removesuffix(".svg") for p in ICON_CACHE.glob("*.svg")}
    missing = wanted - fetched
    if not missing:
        return ICON_CACHE

    def fetch(name: str) -> str | None:
        req = urllib.request.Request(
            ICON_BASE + name + ".svg",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
                )
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
        except Exception:
            return None
        if resp.status != 200 or not data.strip():
            return None
        return data.decode("utf-8")

    for name in sorted(missing):
        data = fetch(name)
        if data is None:
            print(f"warning: could not fetch icon {name}, using {DEFAULT_ICON}.svg")
            if name == DEFAULT_ICON:
                ICON_CACHE.mkdir(parents=True, exist_ok=True)
                (ICON_CACHE / f"{name}.svg").write_text(
                    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"></svg>',
                    encoding="utf-8",
                )
            continue
        (ICON_CACHE / f"{name}.svg").write_text(data, encoding="utf-8")
    print(f"fetched {sorted(missing)} icons into {ICON_CACHE}")
    return ICON_CACHE


def localize_font_links() -> None:
    """Copy cached fonts into SITE and rewrite Google Fonts @imports to the local copy."""
    fonts = SITE / "vendor" / "fonts"
    if not (fonts / "lato.css").is_file():
        fonts.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ensure_fonts(), fonts, dirs_exist_ok=True)
    for css in SITE.rglob("*.css"):
        text = css.read_text(encoding="utf-8")
        if "fonts.googleapis.com" not in text:
            continue
        depth = len(css.relative_to(SITE).parts) - 1
        rel = "../" * depth + "vendor/fonts/lato.css"
        css.write_text(GOOGLE_FONTS_RE.sub(rel, text), encoding="utf-8")


def watch_localize_fonts(stop: threading.Event) -> None:
    """Re-apply localize_font_links() while quarto preview regenerates site assets."""
    while not stop.wait(2):
        try:
            if any(
                "fonts.googleapis.com" in css.read_text(encoding="utf-8")
                for css in SITE.rglob("*.css")
            ):
                localize_font_links()
        except FileNotFoundError:
            pass


def collect(specs: list[tuple[str, pathspec.GitIgnoreSpec]]) -> list[Path]:
    published: list[Path] = []
    src_str = str(SRC)
    for dirpath, dirnames, filenames in os.walk(SRC):
        if dirpath == src_str:
            rel_dir = ""
        else:
            rel_dir = Path(dirpath).relative_to(SRC).as_posix()
        kept_dirs = []
        for d in dirnames:
            rel = f"self/{rel_dir}/{d}" if rel_dir else f"self/{d}"
            if not is_ignored(rel, specs):
                kept_dirs.append(d)
        dirnames[:] = kept_dirs
        for f in filenames:
            if f in (".gitignore", ".siteignore", "__init__.py"):
                continue
            rel = f"self/{rel_dir}/{f}" if rel_dir else f"self/{f}"
            if not is_ignored(rel, specs):
                published.append(Path(dirpath) / f)
    return published


def rel_of(path: Path) -> str:
    return path.relative_to(SRC).as_posix()


def git_date(path: Path, first: bool) -> str | None:
    if first:
        cmd = ["git", "log", "--diff-filter=A", "--format=%aI", "--", str(path)]
    else:
        cmd = ["git", "log", "-1", "--format=%aI", "--", str(path)]
    try:
        out = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, text=True, check=False
        ).stdout.strip()
    except OSError:
        return None
    return out[:10] if out else None


def humanize(name: str) -> str:
    return name.replace("_", " ").replace("-", " ").title()


def slugify(tag: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")


def extract_tags(text: str) -> list[str]:
    tags: list[str] = []
    lines = text.split("\n")
    i = 0
    keyword_re = re.compile(r"^#{2,4}\s*[Kk]eywords\.?\s*:?\s*$")
    while i < len(lines):
        if keyword_re.match(lines[i].strip()):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            while j < len(lines) and lines[j].strip() and not lines[j].lstrip().startswith("#"):
                tag = re.sub(r"^\s*[-*]\s*", "", lines[j]).strip()
                tag = re.sub(r"[.,;:]+$", "", tag)
                if tag:
                    tags.append(tag)
                j += 1
            i = j
        else:
            i += 1
    return tags


def split_front_matter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n", 2)
    if len(lines) < 3 or lines[1].strip() != "---":
        return None, text
    fm_text = lines[1]
    try:
        meta = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        return None, text
    if not isinstance(meta, dict):
        return None, text
    rest = text[len("---\n") + len(fm_text) + len("\n---\n"):]
    return meta, rest


def merge_front_matter(meta: dict | None, body: str) -> str:
    if meta:
        dump = yaml.safe_dump(
            meta, sort_keys=False, allow_unicode=True, default_flow_style=False
        ).rstrip()
        return f"---\n{dump}\n---\n\n{body}"
    return body


class Builder:
    def __init__(self, deploy: bool, preview: bool = False):
        self.deploy = deploy
        self.preview = preview
        self.specs = load_specs(deploy)
        self.published = collect(self.specs)
        self.published_rels = {rel_of(p) for p in self.published}
        self.pages: list[tuple[str, list[str], str]] = []

    def stage(self) -> None:
        STAGE.mkdir(parents=True, exist_ok=True)
        expected: set[str] = set()
        for src in self.published:
            rel = rel_of(src)
            dst = STAGE / rel
            expected.add(rel)
            if src.suffix.lower() == ".md":
                write_if_changed(dst, self.process_md(src))
            else:
                if (
                    not dst.exists()
                    or dst.stat().st_size != src.stat().st_size
                    or dst.stat().st_mtime_ns != src.stat().st_mtime_ns
                ):
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
        root_generated = {"index.qmd", "tags.qmd", "404.qmd", "_quarto.yml"}
        protected = {".quarto", "_freeze", "og", CODE_OUTPUT_DIR}
        for dirpath, dirnames, filenames in os.walk(STAGE):
            dirnames[:] = [d for d in dirnames if d not in protected]
            rel_dir = Path(dirpath).relative_to(STAGE).as_posix()
            for f in filenames:
                if rel_dir == "." and f in root_generated:
                    continue
                rel = f if rel_dir == "." else f"{rel_dir}/{f}"
                if rel not in expected:
                    (Path(dirpath) / f).unlink()
        self.stage_assets()
        self.gen_codeview()
        self.gen_index()
        self.gen_tags()
        self.gen_404()
        self.gen_sidebar_icons()
        self.stage_config(self.preview)

    def process_md(self, src: Path) -> str:
        rel = rel_of(src)
        text = src.read_text(encoding="utf-8")
        meta, body = split_front_matter(text)
        if meta is None:
            meta = {}
        created = git_date(src, first=True)
        modified = git_date(src, first=False)
        if created is None and modified is not None:
            created = modified
        if created:
            meta.setdefault("date", created)
        if modified:
            meta["date-modified"] = modified
        tags = meta.get("categories") or meta.get("keywords") or []
        if isinstance(tags, str):
            tags = [tags]
        tags = [str(t) for t in tags]
        for tag in extract_tags(body):
            if tag not in tags:
                tags.append(tag)
        meta.pop("keywords", None)
        if tags:
            meta["categories"] = tags
        parts = rel.split("/")
        if len(parts) > 1:
            img = f"{SITE_URL}og/{slugify(parts[0])}.png"
            meta.setdefault("image", img)
        body = self.rewrite_links(body, str(Path(rel).parent))
        block = [".page-meta"]
        if modified:
            block.append(f"**Last updated:** {modified}")
        links = []
        for tag in tags:
            slug = slugify(tag)
            depth = len(Path(rel).parts) - 1
            href = "../" * depth + "tags.html#" + slug
            links.append(f"[`{tag}`]({href})")
        if links:
            block.append("**Keywords:** " + " · ".join(links))
        if len(block) > 1:
            body = "::: {.page-meta}\n" + "\n\n".join(block[1:]) + "\n:::\n\n" + body
        self.pages.append((rel, tags, created or ""))
        return merge_front_matter(meta, body)

    def rewrite_links(self, text: str, page_dir: str) -> str:
        def rep(m: re.Match) -> str:
            target = m.group(2)
            head, sep, tail = target.partition("#")
            head, _, query = head.partition("?")
            if not head or head.startswith(("/", "#", "http://", "https://", "mailto:")):
                return m.group(0)
            if Path(head).suffix.lower() not in CODE_EXTENSIONS:
                return m.group(0)
            resolved = os.path.normpath(os.path.join(page_dir, head))
            if resolved not in self.published_rels:
                return m.group(0)
            code_page = os.path.join(CODE_OUTPUT_DIR, resolved + ".qmd")
            new = os.path.relpath(code_page, page_dir)
            return m.group(1) + new + (f"?{query}" if query else "") + (f"#{tail}" if sep else "") + ")"

        text = MD_LINK_RE.sub(rep, text)

        def rep_href(m: re.Match) -> str:
            target = m.group(2)
            head, sep, tail = target.partition("#")
            head, _, query = head.partition("?")
            if not head or head.startswith(("/", "#", "http://", "https://", "mailto:")):
                return m.group(0)
            if Path(head).suffix.lower() not in CODE_EXTENSIONS:
                return m.group(0)
            resolved = os.path.normpath(os.path.join(page_dir, head))
            if resolved not in self.published_rels:
                return m.group(0)
            code_page = os.path.join(CODE_OUTPUT_DIR, resolved + ".qmd")
            new = os.path.relpath(code_page, page_dir)
            return m.group(1) + new + (f"?{query}" if query else "") + (f"#{tail}" if sep else "") + m.group(3)

        return HREF_RE.sub(rep_href, text)

    def gen_codeview(self) -> None:
        generated: set[str] = set()
        for src in self.published:
            ext = src.suffix.lower()
            if ext not in CODE_EXTENSIONS:
                continue
            rel = rel_of(src)
            try:
                data = src.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "\x00" in data:
                continue
            lang = LANGS.get(ext, "text")
            if rel.endswith((".lock",)) and src.name in ("Cargo.lock", "uv.lock"):
                lang = "toml"
            run = max((len(m) for m in re.findall(r"`+", data)), default=0)
            fence = "`" * max(3, run + 1)
            page_dir = os.path.join(CODE_OUTPUT_DIR, str(Path(rel).parent))
            download = os.path.relpath(rel, page_dir)
            title = src.name
            content = (
                "---\n"
                f'title: "{title}"\n'
                "---\n\n"
                f"**Path:** `{rel}` · [Download raw file]({download})\n\n"
                f"{fence}{{{'.' + lang}}}\n"
                f"{data.rstrip()}\n"
                f"{fence}\n"
            )
            rel_qmd = os.path.join(CODE_OUTPUT_DIR, f"{rel}.qmd")
            generated.add(rel_qmd)
            write_if_changed(STAGE / rel_qmd, content)
            self.pages.append((rel_qmd, [], ""))
        cvd = STAGE / CODE_OUTPUT_DIR
        if cvd.is_dir():
            for p in cvd.rglob("*.qmd"):
                if p.relative_to(STAGE).as_posix() not in generated:
                    p.unlink()

    def tree(self) -> dict:
        tree: dict = {"dirs": {}, "files": []}

        def add(parts: list[str], kind: str, href: str) -> None:
            node = tree
            for part in parts[:-1]:
                node = node["dirs"].setdefault(part, {"dirs": {}, "files": []})
            node["files"].append((kind, parts[-1], href))

        for p in sorted(self.published, key=lambda x: rel_of(x).lower()):
            rel = rel_of(p)
            ext = p.suffix.lower()
            parts = rel.split("/")
            if ext == ".md":
                add(parts, "md", rel)
            elif ext == ".ipynb":
                add(parts, "nb", rel)
            elif ext in CODE_EXTENSIONS:
                add(parts, "code", f"{CODE_OUTPUT_DIR}/{rel}.qmd")
            else:
                add(parts, "file", rel)
        return tree

    def sidebar_contents(self) -> list[dict]:
        tree = self.tree()
        out: list[dict] = [{"href": "index.qmd"}]

        def file_entry(kind: str, name: str, href: str) -> dict:
            return {"href": href, "text": name}

        def section(label: str, node: dict) -> dict | None:
            entry: dict = {"section": label, "contents": []}
            for name, child in sorted(node["dirs"].items(), key=lambda kv: kv[0].lower()):
                sub = section(humanize(name), child)
                if sub is not None:
                    entry["contents"].append(sub)
            page_files = [f for f in node["files"] if f[0] != "file"]
            for kind, name, href in sorted(page_files, key=lambda f: f[1].lower()):
                entry["contents"].append(file_entry(kind, name, href))
            return entry if entry["contents"] else None

        for name, node in sorted(tree["dirs"].items(), key=lambda kv: kv[0].lower()):
            item = section(humanize(name), node)
            if item is not None:
                out.append(item)
        page_files = [f for f in tree["files"] if f[0] != "file"]
        for kind, name, href in sorted(page_files, key=lambda f: f[1].lower()):
            out.append(file_entry(kind, name, href))
        out.append({"href": "tags.qmd"})
        return out

    def stage_config(self, preview: bool = False) -> None:
        text = CONFIG.read_text(encoding="utf-8")
        config = yaml.safe_load(text)
        config["project"]["output-dir"] = "../site"
        config["website"]["sidebar"] = {
            "style": "docked",
            "contents": self.sidebar_contents(),
        }
        config["format"]["html"]["css"] = ["styles.css"]
        config["format"]["html"]["include-in-header"] = ["sidebar-icons.html"]
        write_if_changed(STAGE / "styles.css", (ROOT / "site_tools" / "styles.css").read_text(encoding="utf-8"))
        if preview:
            config["format"]["html"]["html-math-method"] = {
                "method": "katex",
                "url": "/vendor/katex/",
            }
        write_if_changed(
            STAGE / "_quarto.yml",
            yaml.safe_dump(config, sort_keys=False, allow_unicode=True, default_flow_style=False),
        )

    def stage_assets(self) -> None:
        og_dir = STAGE / "og"
        og_dir.mkdir(parents=True, exist_ok=True)
        projects = sorted({rel_of(p).split("/")[0] for p in self.published if "/" in rel_of(p)})
        for project in projects:
            img = og_dir / f"{slugify(project)}.png"
            if not img.exists():
                self.make_og(img, humanize(project))

    def make_og(self, path: Path, label: str) -> None:
        from PIL import Image, ImageDraw, ImageFont

        width, height = 1200, 630
        digest = hashlib.sha256(str(path.stem).encode()).hexdigest()
        bg = tuple(int(digest[i:i + 2], 16) for i in (0, 2, 4))
        img = Image.new("RGB", (width, height), bg)
        draw = ImageDraw.Draw(img)
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
        title_font = None
        small_font = None
        for fp in font_paths:
            if os.path.exists(fp):
                title_font = ImageFont.truetype(fp, 96)
                small_font = ImageFont.truetype(fp, 40)
                break
        if title_font is None:
            title_font = ImageFont.load_default(size=64)
            small_font = ImageFont.load_default(size=32)
        words = label.split()
        lines = []
        current = ""
        for word in words:
            if current and draw.textlength(current + " " + word, font=title_font) > width - 160:
                lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        y = height // 2 - 40 * max(1, len(lines) // 2)
        primer = (255, 255, 255)
        for line in lines[:4]:
            text_width = draw.textlength(line, font=title_font)
            draw.text(((width - text_width) / 2, y), line, font=title_font, fill=primer)
            y += 110
        brand = "DIRECTED ARTICLES"
        brand_width = draw.textlength(brand, font=small_font)
        draw.text(((width - brand_width) / 2, height - 90), brand, font=small_font, fill=(230, 230, 230))
        img.save(path, format="PNG")

    def gen_index(self) -> None:
        lines = [
            "---",
            'title: "Directed Articles"',
            "---",
            "",
            "Directed Articles.",
            "",
        ]
        tree = self.tree()

        def walk(node: dict) -> list[tuple[str, str, str]]:
            out: list[tuple[str, str, str]] = []
            for child in node["dirs"].values():
                out.extend(walk(child))
            out.extend(sorted(node["files"], key=lambda f: f[1].lower()))
            return out

        for name, node in sorted(tree["dirs"].items(), key=lambda kv: kv[0].lower()):
            lines.append(f"## {humanize(name)}")
            lines.append("")
            for kind, fname, href in walk(node):
                lines.append(f"- [{fname}]({href})")
            lines.append("")
        lines.append("## Site")
        lines.append("")
        lines.append("- [Tag index](tags.html)")
        lines.append("")
        write_if_changed(STAGE / "index.qmd", "\n".join(lines))

    def gen_tags(self) -> None:
        tag_map: dict[str, tuple[str, list[tuple[str, str]]]] = {}
        for rel, tags, _ in self.pages:
            for tag in sorted(set(tags), key=slugify):
                slug = slugify(tag)
                label = Path(rel).stem.replace("_", " ").replace("-", " ").title()
                tag_map.setdefault(slug, (tag, []))[1].append((label, rel))
        lines = [
            "---",
            'title: "Tags"',
            "---",
            "",
        ]
        for slug in sorted(tag_map):
            tag, entries = tag_map[slug]
            entries = sorted(set(entries), key=lambda e: e[0].lower())
            lines.append(f"## {tag} {{#{slug}}}")
            lines.append("")
            for label, href in entries:
                lines.append(f"- [{label}]({href})")
            lines.append("")
        write_if_changed(STAGE / "tags.qmd", "\n".join(lines))

    def gen_404(self) -> None:
        content = (
            "---\n"
            'title: "Not found"\n'
            "---\n\n"
            "This page does not exist (or was excluded from the published site).\n\n"
            "[Back to the index](index.html)\n"
        )
        write_if_changed(STAGE / "404.qmd", content)

    def render(self) -> None:
        if SITE.exists():
            shutil.rmtree(SITE)
        result = subprocess.run(
            ["quarto", "render", str(STAGE)], cwd=ROOT, text=True, check=False
        )
        if result.returncode != 0:
            sys.exit(f"quarto render failed with exit code {result.returncode}")

    def icon_map(self) -> dict[str, str]:
        icon_map: dict[str, str] = {}
        for src in self.published:
            rel = rel_of(src)
            ext = src.suffix.lower()
            if ext == ".md":
                href = os.path.splitext(rel)[0] + ".html"
                icon = EXT_ICONS[".md"]
            elif ext == ".ipynb":
                href = os.path.splitext(rel)[0] + ".html"
                icon = EXT_ICONS[".ipynb"]
            elif ext in CODE_EXTENSIONS:
                href = f"{CODE_OUTPUT_DIR}/{rel}.html"
                icon = LOCK_ICONS.get(src.name) or EXT_ICONS.get(ext, DEFAULT_ICON)
            else:
                continue
            icon_map[href] = icon
        return icon_map

    def gen_sidebar_icons(self) -> None:
        """Write a script (inlined into every page header) that attaches the
        per-extension icon to each sidebar file entry on page load."""
        icons = json.dumps(self.icon_map())
        if icons == "{}":
            write_if_changed(STAGE / "sidebar-icons.html", "")
            return
        script = (
            "<script>\n"
            "(function () {\n"
            "  var icons = " + icons + ";\n"
            "  function attachIcons() {\n"
            "    var css = document.querySelector('link[href$=\"styles.css\"]');\n"
            "    if (!css) return;\n"
            "    var base = css.href.slice(0, css.href.lastIndexOf('/') + 1);\n"
            "    var links = document.querySelectorAll(\n"
            "      '#quarto-sidebar a.sidebar-item-text[href]'\n"
            "    );\n"
            "    for (var i = 0; i < links.length; i++) {\n"
            "      var a = links[i];\n"
            "      if (a.querySelector('img.sidebar-file-icon')) continue;\n"
            "      var icon = null;\n"
            "      for (var key in icons) {\n"
            "        if (a.href === base + key) { icon = icons[key]; break; }\n"
            "      }\n"
            "      if (!icon) continue;\n"
            "      var img = document.createElement('img');\n"
            "      img.src = base + 'icons/' + icon + '.svg';\n"
            "      img.className = 'sidebar-file-icon';\n"
            "      img.alt = '';\n"
            "      var text = a.querySelector('.menu-text');\n"
            "      if (text) a.insertBefore(img, text); else a.appendChild(img);\n"
            "    }\n"
            "  }\n"
            "  if (document.readyState === 'loading') {\n"
            "    document.addEventListener('DOMContentLoaded', attachIcons);\n"
            "  } else {\n"
            "    attachIcons();\n"
            "  }\n"
            "})();\n"
            "</script>\n"
        )
        write_if_changed(STAGE / "sidebar-icons.html", script)

    def sync_icons(self) -> None:
        if not SITE.exists():
            return
        ensure_file_icons(set(self.icon_map().values()))
        icons = SITE / "icons"
        icons.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ICON_CACHE, icons, dirs_exist_ok=True)

    def postprocess(self) -> None:
        if not SITE.exists():
            return
        vendor_dir = SITE / "vendor"
        vendor_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ensure_katex(), vendor_dir / "katex", dirs_exist_ok=True)
        localize_font_links()
        self.sync_icons()
        og = STAGE / "og"
        if og.exists():
            shutil.copytree(og, SITE / "og", dirs_exist_ok=True)
        for html in SITE.rglob("*.html"):
            text = html.read_text(encoding="utf-8")
            depth = len(html.relative_to(SITE).parts) - 1
            rel = "../" * depth
            text = KATEX_CDN_RE.sub(lambda m: f"{rel}vendor/katex/{m.group(1)}", text)
            text = POLYFILL_RE.sub("", text)
            html.write_text(text, encoding="utf-8")
            cdn = CDN_RE.findall(text)
            if cdn:
                message = f"remaining CDN references in {html}: {cdn}"
                if self.deploy:
                    sys.exit(message)
                print(f"warning: {message}", file=sys.stderr)
        for css in SITE.rglob("*.css"):
            cdn = CDN_RE.findall(css.read_text(encoding="utf-8"))
            if cdn:
                message = f"remaining CDN references in {css}: {cdn}"
                if self.deploy:
                    sys.exit(message)
                print(f"warning: {message}", file=sys.stderr)

    def summary(self) -> None:
        n_pages = len(list(SITE.rglob("*.html")))
        n_code = sum(1 for rel, _, _ in self.pages if rel.startswith(CODE_OUTPUT_DIR))
        n_md = sum(1 for rel, _, _ in self.pages if rel.endswith(".md"))
        n_tags = len({slugify(t) for _, tags, _ in self.pages for t in tags})
        print(f"rendered {n_pages} pages ({n_md} markdown, {n_code} code views), {n_tags} tags")

    def stale_outputs(self) -> list[Path]:
        if not SITE.exists():
            return [
                p for p in STAGE.rglob("*")
                if p.is_file() and p.suffix.lower() in (".qmd", ".md")
            ]
        stale: list[Path] = []
        for q in STAGE.rglob("*"):
            if not q.is_file() or q.suffix.lower() not in (".qmd", ".md"):
                continue
            out = SITE / q.relative_to(STAGE).with_suffix(".html")
            if not out.exists() or out.stat().st_mtime_ns < q.stat().st_mtime_ns:
                stale.append(q)
        return stale

    def touch_outputs(self) -> None:
        now = time.time_ns()
        for html in SITE.rglob("*.html"):
            os.utime(html, ns=(now, now))

    def render_stale(self, stale: list[Path]) -> None:
        for q in stale:
            result = subprocess.run(
                ["quarto", "render", str(q)], cwd=ROOT, text=True, check=False
            )
            if result.returncode != 0:
                sys.exit(f"quarto render {q} failed with exit code {result.returncode}")

    def config_changed(self) -> bool:
        cfg = STAGE / "_quarto.yml"
        if not cfg.is_file() or not SITE.exists():
            return True
        cfg_ns = cfg.stat().st_mtime_ns
        return any(cfg_ns > h.stat().st_mtime_ns for h in SITE.rglob("*.html"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Stage self/ into a Quarto website project, render it to site/ and "
        "vendor runtime assets (KaTeX)."
    )
    parser.add_argument("--deploy", action="store_true", help="apply .siteignore exclusions")
    parser.add_argument("--stage-only", action="store_true", help="build quarto_src/ without rendering")
    parser.add_argument("--preview", action="store_true", help="stage then run quarto preview on quarto_src/")
    args = parser.parse_args()
    deploy = args.deploy or os.environ.get(DEPLOY_ENV, "").lower() == "true"
    builder = Builder(deploy, preview=args.preview)
    builder.stage()
    print(f"staged {len(builder.published)} published files into {STAGE}")
    if not args.stage_only:
        if args.preview:
            stale = builder.stale_outputs()
            if stale and (builder.config_changed() or len(stale) > 10):
                print(f"preview: full render ({len(stale)} stale files)")
                builder.render()
            elif stale:
                print(f"preview: rendering {len(stale)} stale file(s)")
                builder.render_stale(stale)
            else:
                print("preview: outputs up to date, skipping render")
            vendor_dir = SITE / "vendor"
            vendor_dir.mkdir(parents=True, exist_ok=True)
            shutil.copytree(ensure_katex(), vendor_dir / "katex", dirs_exist_ok=True)
            localize_font_links()
            builder.sync_icons()
            stop = threading.Event()
            threading.Thread(target=watch_localize_fonts, args=(stop,), daemon=True).start()
            builder.touch_outputs()
            subprocess.run(["quarto", "preview", str(STAGE)], cwd=ROOT, check=False)
            stop.set()
        else:
            builder.render()
            builder.postprocess()
            builder.summary()


if __name__ == "__main__":
    main()