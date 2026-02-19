"""Logging setup for template projects."""

from __future__ import annotations

import logging


def configure_logging(level: str = "INFO") -> None:
    """Configure basic logging for command-line runs."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
