from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files, InclusionLevel

from site_tools.codeview_plugin import CODE_OUTPUT_DIR

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig

logger = logging.getLogger(__name__)


class FileBrowserPlugin(BasePlugin):
    """Generate the root index page listing every file in the site.

    Folder listing pages are not generated: folders are containers in the
    sidebar, only files (markdown pages and code files) represent content.
    """

    config_scheme = (
        ("hidden_dirs", c.Type(list, default=["javascripts"])),
    )

    def on_files(self, files: Files, config: "MkDocsConfig") -> "Files":
        hidden = set(self.config["hidden_dirs"])
        docs_dir = config["docs_dir"]
        tree: dict[str, Any] = {"files": {}, "dirs": {}}
        for file in files:
            if not file.inclusion.is_included():
                continue
            if Path(file.src_dir) != Path(docs_dir):
                continue
            parts = Path(file.src_uri).parts
            if parts[0] == CODE_OUTPUT_DIR:
                continue
            if getattr(file, "_browser_skip", False):
                continue
            node = tree
            for part in parts[:-1]:
                node = node["dirs"].setdefault(part, {"files": {}, "dirs": {}})
            node["files"][parts[-1]] = file

        def humanize(name: str) -> str:
            return name.replace("_", " ").replace("-", " ").title()

        def collect(node: dict[str, Any], path: list[str]) -> list[tuple[str, File]]:
            entries = []
            for name, child in sorted(node["dirs"].items(), key=lambda kv: kv[0].lower()):
                if name in hidden:
                    continue
                entries.extend(collect(child, path + [name]))
            for name, file in sorted(node["files"].items(), key=lambda kv: kv[0].lower()):
                entries.append(("/".join(path + [name]), file))
            return entries

        lines = [f"# {config['site_name']}", ""]
        for name, file in sorted(tree["files"].items(), key=lambda kv: kv[0].lower()):
            if name == "index.md":
                continue
            code_page = getattr(file, "_code_page", None)
            target = code_page.src_uri if code_page is not None else file.src_uri
            lines.append(f"- [{name}]({target})")
        if lines[-1]:
            lines.append("")
        for name, child in sorted(tree["dirs"].items(), key=lambda kv: kv[0].lower()):
            if name in hidden:
                continue
            entries = collect(child, [name])
            if not entries:
                continue
            lines.append(f"## {humanize(name)}")
            lines.append("")
            for display, file in entries:
                code_page = getattr(file, "_code_page", None)
                target = code_page.src_uri if code_page is not None else file.src_uri
                lines.append(f"- [{display}]({target})")
            lines.append("")

        index = File(
            "index.md",
            config["docs_dir"],
            config["site_dir"],
            config["use_directory_urls"],
            inclusion=InclusionLevel.INCLUDED,
        )
        index.generated_by = "filebrowser"
        index.content_string = "\n".join(lines) + "\n"
        files.append(index)
        logger.info("Generated root index page")
        return files
