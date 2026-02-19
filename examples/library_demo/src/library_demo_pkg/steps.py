"""Pipeline steps for the library template."""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from .api import summarize_values

if TYPE_CHECKING:
    from .pipeline import PipelineContext

LOGGER = logging.getLogger(__name__)


class SummarizeValuesStep:
    """Summarize configured values and emit an artifact."""

    name = "summarize_values"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Compute a summary and persist it as JSON."""
        summary = summarize_values(ctx.config.get("values", []))
        artifact_path = ctx.run_dir / ctx.config["artifact_filename"]
        artifact_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        ctx.artifacts["artifact_path"] = str(artifact_path)
        ctx.metrics["value_count"] = summary["count"]
        ctx.metrics["value_sum"] = summary["sum"]
        ctx.metrics["value_mean"] = summary["mean"]
        LOGGER.info("Summary written: %s", artifact_path)
        return ctx


class PersistMetricsStep:
    """Persist metrics dictionary as JSON artifact."""

    name = "persist_metrics"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Write metrics to disk for reproducibility."""
        metrics_path = ctx.run_dir / "metrics.json"
        metrics_path.write_text(json.dumps(ctx.metrics, indent=2), encoding="utf-8")
        ctx.artifacts["metrics_path"] = str(metrics_path)
        LOGGER.info("Metrics written: %s", metrics_path)
        return ctx
