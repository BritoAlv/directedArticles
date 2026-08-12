from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

import pathspec

from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import InclusionLevel

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files

logger = logging.getLogger(__name__)


class GitignorePlugin(BasePlugin):
    def on_files(self, files: "Files", config: "MkDocsConfig") -> "Files":
        config_dir = Path(config.config_file_path).parent
        gitignore_path = config_dir / ".gitignore"
        if not gitignore_path.is_file():
            return files
        spec = pathspec.GitIgnoreSpec.from_lines(
            gitignore_path.read_text(encoding="utf-8").splitlines()
        )
        root = config_dir.resolve()
        docs_dir = Path(config["docs_dir"]).resolve()
        prefix = docs_dir.relative_to(root).as_posix()
        for file in files:
            if not file.inclusion.is_included():
                continue
            rel = f"{prefix}/{file.src_uri}"
            if spec.match_file(rel):
                logger.info("Excluding '%s' (matches .gitignore)", rel)
                file.inclusion = InclusionLevel.EXCLUDED
        return files
