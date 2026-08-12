from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

import pathspec

from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import InclusionLevel

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files

logger = logging.getLogger(__name__)

_SITE_DEPLOY_VAR = "MKDOCS_DEPLOY"


class GitignorePlugin(BasePlugin):
    def on_files(self, files: "Files", config: "MkDocsConfig") -> "Files":
        config_dir = Path(config.config_file_path).parent
        root = config_dir.resolve()
        docs_dir = Path(config["docs_dir"]).resolve()
        prefix = docs_dir.relative_to(root).as_posix()

        ignore_specs: list[tuple[str, pathspec.GitIgnoreSpec]] = []

        def add_ignore_file(path: Path) -> None:
            if not path.is_file():
                return
            lines = path.read_text(encoding="utf-8").splitlines()
            if not lines:
                return
            spec = pathspec.GitIgnoreSpec.from_lines(lines)
            base = path.parent.resolve().relative_to(root).as_posix()
            ignore_specs.append((base, spec))

        add_ignore_file(config_dir / ".gitignore")
        for path in docs_dir.rglob(".gitignore"):
            add_ignore_file(path)
        if os.environ.get(_SITE_DEPLOY_VAR):
            add_ignore_file(config_dir / ".siteignore")

        if not ignore_specs:
            return files

        for file in files:
            if not file.inclusion.is_included():
                continue

            rel = f"{prefix}/{file.src_uri}"
            for base, spec in ignore_specs:
                if base:
                    if rel != base and not rel.startswith(f"{base}/"):
                        continue
                    local_rel = rel[len(base) :].lstrip("/")
                else:
                    local_rel = rel
                if spec.match_file(local_rel):
                    logger.info("Excluding '%s'", rel)
                    file.inclusion = InclusionLevel.EXCLUDED
                    break
        return files
