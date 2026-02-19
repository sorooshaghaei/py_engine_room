"""Pipeline steps for the app template."""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pipeline import PipelineContext

LOGGER = logging.getLogger(__name__)


class CreateArtifactStep:
    """Create a small artifact to prove end-to-end execution."""

    name = "create_artifact"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Write an artifact file and register its path."""
        payload = {
            "run_name": ctx.config["run_name"],
            "root_dir": str(ctx.root_dir),
            "run_dir": str(ctx.run_dir),
        }
        artifact_path = ctx.run_dir / ctx.config["artifact_filename"]
        artifact_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        ctx.artifacts["artifact_path"] = str(artifact_path)
        LOGGER.info("Artifact written: %s", artifact_path)
        return ctx


class CaptureMetricsStep:
    """Populate a tiny metrics dictionary."""

    name = "capture_metrics"

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Record deterministic example metrics."""
        ctx.metrics["items_written"] = 1.0
        ctx.metrics["steps_executed"] = 2.0
        LOGGER.info("Metrics captured: %s", ctx.metrics)
        return ctx
