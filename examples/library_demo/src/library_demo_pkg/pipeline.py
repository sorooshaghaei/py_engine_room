"""Pipeline scaffold shared across template variants."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

LOGGER = logging.getLogger(__name__)


@dataclass
class PipelineContext:
    """Context object passed through every pipeline step."""

    root_dir: Path
    run_dir: Path
    config: dict[str, Any]
    artifacts: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)


class PipelineStep(Protocol):
    """Protocol that every pipeline step must satisfy."""

    name: str

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Execute the step and return the updated context."""


def build_default_steps() -> list[PipelineStep]:
    """Return a minimal runnable step sequence."""
    from .steps import PersistMetricsStep, SummarizeValuesStep

    return [SummarizeValuesStep(), PersistMetricsStep()]


def run_pipeline(config: dict[str, Any], steps: list[PipelineStep] | None = None) -> PipelineContext:
    """Run the pipeline from configuration and return the final context."""
    root_dir = Path(config["root_dir"]).resolve()
    run_dir = root_dir / "outputs" / str(config["run_name"])
    run_dir.mkdir(parents=True, exist_ok=True)

    ctx = PipelineContext(root_dir=root_dir, run_dir=run_dir, config=config)
    pipeline_steps = steps if steps is not None else build_default_steps()

    for step in pipeline_steps:
        LOGGER.info("Running step: %s", step.name)
        ctx = step.run(ctx)

    return ctx
