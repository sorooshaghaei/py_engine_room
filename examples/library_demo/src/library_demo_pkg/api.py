"""Pure reusable functions for library consumers."""

from __future__ import annotations

from typing import Sequence


def summarize_values(values: Sequence[float]) -> dict[str, float]:
    """Return count, sum, and mean for numeric values."""
    count = float(len(values))
    total = float(sum(values))
    mean = total / count if count else 0.0
    return {"count": count, "sum": total, "mean": mean}
