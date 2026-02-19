"""Configuration loader helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    """Load YAML config and apply minimal defaults."""
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as file:
        raw = yaml.safe_load(file) or {}

    config = dict(raw)
    config.setdefault("run_name", "local-run")
    config.setdefault("root_dir", ".")
    config.setdefault("artifact_filename", "notes_summary.md")
    config.setdefault("notes", ["observation"])
    config.setdefault("log_level", "INFO")
    return config
