"""Thin command-line entrypoint for the app template."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from template_pkg.config import load_config
from template_pkg.logging_utils import configure_logging
from template_pkg.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for pipeline execution."""
    parser = argparse.ArgumentParser(description="Run the app template pipeline.")
    parser.add_argument("--config", type=Path, required=True, help="Path to a YAML config file.")
    return parser.parse_args()


def main() -> int:
    """Execute the configured pipeline and return an exit code."""
    args = parse_args()
    config = load_config(args.config)
    configure_logging(config.get("log_level", "INFO"))

    try:
        run_pipeline(config)
    except Exception:
        logging.exception("Pipeline execution failed")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
