"""Helpers that should be imported by notebooks and scripts."""

from __future__ import annotations

from typing import Sequence


def summarize_notes(notes: Sequence[str]) -> str:
    """Build a compact markdown summary from note labels."""
    lines = ["# Research Summary", ""]
    for index, note in enumerate(notes, start=1):
        lines.append(f"{index}. {note}")
    return "\n".join(lines) + "\n"
