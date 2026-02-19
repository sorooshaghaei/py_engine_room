"""Pipeline steps for the research template."""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from .research_helpers import summarize_notes

if TYPE_CHECKING:
    from .pipeline import PipelineContext

LOGGER = logging.getLogger(__name__)


class BuildSummaryStep:
    """Create markdown summary from configured notes."""

    name = "build_summary"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Write markdown artifact for reproducible reporting."""
        text = summarize_notes(ctx.config.get("notes", []))
        artifact_path = ctx.run_dir / ctx.config["artifact_filename"]
        artifact_path.write_text(text, encoding="utf-8")
        ctx.artifacts["summary_path"] = str(artifact_path)
        ctx.metrics["note_count"] = float(len(ctx.config.get("notes", [])))
        LOGGER.info("Summary written: %s", artifact_path)
        return ctx


class SaveMetricsStep:
    """Persist metrics as JSON artifact."""

    name = "save_metrics"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Write metrics artifact for quick comparison across runs."""
        metrics_path = ctx.run_dir / "metrics.json"
        metrics_path.write_text(json.dumps(ctx.metrics, indent=2), encoding="utf-8")
        ctx.artifacts["metrics_path"] = str(metrics_path)
        LOGGER.info("Metrics written: %s", metrics_path)
        return ctx
