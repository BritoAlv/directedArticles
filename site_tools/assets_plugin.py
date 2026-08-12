from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files, InclusionLevel

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig

logger = logging.getLogger(__name__)


class AssetsPlugin(BasePlugin):
    config_scheme = (
        ("files", c.Type(dict, default={})),
    )

    def on_files(self, files: Files, config: "MkDocsConfig") -> "Files":
        base = Path(config.config_file_path).parent
        for url, src in self.config["files"].items():
            path = base / src
            if path.is_dir():
                for child in sorted(path.iterdir()):
                    if child.is_file():
                        self._inject(files, config, f"{url.rstrip('/')}/{child.name}", child)
            elif path.is_file():
                self._inject(files, config, url, path)
            else:
                logger.warning("Assets plugin: source not found: %s", path)
        return files

    def _inject(
        self, files: Files, config: "MkDocsConfig", url: str, path: Path
    ) -> None:
        f = File(
            url,
            config["docs_dir"],
            config["site_dir"],
            config["use_directory_urls"],
            inclusion=InclusionLevel.INCLUDED,
        )
        f.generated_by = "assets"
        f.content_bytes = path.read_bytes()
        f._browser_skip = True
        files.append(f)
        logger.info("Injected asset '%s' from '%s'", url, path)
