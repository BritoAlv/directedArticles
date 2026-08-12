from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files, InclusionLevel
from mkdocs.utils import get_relative_url

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig

logger = logging.getLogger(__name__)

CODE_OUTPUT_DIR = "__code__"

CODE_EXTENSIONS = {
    ".rs",
    ".py",
    ".toml",
    ".sh",
    ".bash",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".json",
    ".yml",
    ".yaml",
    ".c",
    ".h",
    ".cpp",
    ".hpp",
    ".java",
    ".go",
    ".rb",
    ".txt",
    ".ini",
    ".cfg",
    ".sql",
    ".html",
    ".css",
    ".lock",
}


class CodeViewPlugin(BasePlugin):
    config_scheme = (
        ("hidden_dirs", c.Type(list, default=["javascripts"])),
    )

    def on_files(self, files: Files, config: "MkDocsConfig") -> "Files":
        hidden = set(self.config["hidden_dirs"])
        docs_dir = config["docs_dir"]
        for file in list(files):
            if not file.inclusion.is_included():
                continue
            if getattr(file, "_browser_skip", False):
                continue
            if Path(file.src_dir) != Path(docs_dir):
                continue
            parts = file.src_uri.split("/")
            if parts[0] in hidden or parts[0] == CODE_OUTPUT_DIR:
                continue
            if Path(file.src_uri).suffix.lower() not in CODE_EXTENSIONS:
                continue
            try:
                content = file.content_string
            except OSError:
                continue
            if "\x00" in content:
                continue

            try:
                name = Path(file.src_uri).name
                if name in ("Cargo.lock", "uv.lock"):
                    lexer = get_lexer_for_filename("Cargo.toml")
                else:
                    lexer = get_lexer_for_filename(file.src_uri)
            except ClassNotFound:
                lexer = None
            lang = lexer.aliases[0] if lexer and lexer.aliases else "text"

            run = max((len(m) for m in re.findall(r"`+", content)), default=0)
            fence = "`" * max(3, run + 1)

            code_src = f"{CODE_OUTPUT_DIR}/{file.src_uri}.md"
            raw_rel = os.path.relpath(file.src_uri, start=os.path.dirname(code_src))
            page = File(
                code_src,
                docs_dir,
                config["site_dir"],
                config["use_directory_urls"],
                inclusion=InclusionLevel.NOT_IN_NAV,
            )
            page.generated_by = "codeview"
            page.content_string = (
                f"# {Path(file.src_uri).name}\n\n"
                f"**Path:** `{file.src_uri}` · "
                f"[Download raw file]({raw_rel})\n\n"
                f"{fence}{lang} linenums=\"1\"\n"
                f"{content.rstrip()}\n"
                f"{fence}\n"
            )
            file._code_page = page
            files.append(page)
            logger.info("Generated code page for '%s'", file.src_uri)
        return files

    def on_page_content(self, html: str, page, config: "MkDocsConfig", files: "Files") -> str:
        """Rewrite links to code files so they open the highlighted code page."""

        base = os.path.dirname(page.file.url)

        def rewrite(match: re.Match) -> str:
            href = match.group(2)
            if href.startswith(("#", "/", "http://", "https://", "mailto:")):
                return match.group(0)
            path = href.split("#", 1)[0].split("?", 1)[0]
            if not path:
                return match.group(0)
            resolved = os.path.normpath(os.path.join(base, path))
            target = files.get_file_from_path(resolved)
            if target is None or not hasattr(target, "_code_page"):
                return match.group(0)
            if target._code_page == page.file:
                return match.group(0)
            new_path = get_relative_url(target._code_page.url, page.file.url)
            return f'{match.group(1)}{new_path}{href[len(path):]}{match.group(3)}'

        return re.sub(r'(<a\s[^>]*?href=["\'])([^"\']*)(["\'])', rewrite, html)
