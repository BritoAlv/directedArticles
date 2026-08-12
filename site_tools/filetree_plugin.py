from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page

from site_tools.codeview_plugin import CODE_OUTPUT_DIR

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files

logger = logging.getLogger(__name__)


def humanize(name: str) -> str:
    return name.replace("_", " ").replace("-", " ").title()


class FileTreePlugin(BasePlugin):
    """Replace the mkdocs navigation with a file-explorer style tree.

    The sidebar mirrors the docs directory: every folder becomes a section
    (clickable when it has a filebrowser index page, thanks to
    `navigation.indexes`) and every file becomes a leaf item. Code files link
    to their generated code pages, like in a VS Code file explorer.
    """

    config_scheme = (
        ("hidden_dirs", c.Type(list, default=["javascripts"])),
    )

    def on_nav(self, nav, config: "MkDocsConfig", files: "Files"):
        docs_dir = Path(config["docs_dir"])
        hidden = set(self.config["hidden_dirs"])

        tree: dict[str, dict | Page] = {}
        for file in files:
            if not file.inclusion.is_included():
                continue
            if Path(file.src_dir) != docs_dir:
                continue
            if getattr(file, "generated_by", None) == "filebrowser":
                continue
            parts = file.src_uri.split("/")
            if parts[0] == CODE_OUTPUT_DIR or parts[0] in hidden:
                continue
            if getattr(file, "_browser_skip", False):
                continue
            page = file.page
            if page is None:
                code = getattr(file, "_code_page", None)
                if code is None:
                    continue
                page = code.page
            if page is None:
                continue
            node = tree
            for part in parts[:-1]:
                child = node.get(part)
                if not isinstance(child, dict):
                    child = node[part] = {}
                node = child
            node[parts[-1]] = page

        def build(node: dict, prefix: str) -> list:
            items: list = []
            for name, child in sorted(
                node.items(),
                key=lambda kv: (0 if isinstance(kv[1], dict) else 1, kv[0].lower()),
            ):
                if isinstance(child, dict):
                    sub_prefix = f"{prefix}/{name}" if prefix else name
                    children = build(child, sub_prefix)
                    if not children:
                        continue
                    section = Section(title=humanize(name), children=children)
                    for item in children:
                        item.parent = section
                    items.append(section)
                else:
                    child.title = name
                    items.append(child)
            return items

        nav.items = build(tree, "")
        return nav
