"""Public package API for the research template."""

from .pipeline import PipelineContext, PipelineStep, run_pipeline
from .research_helpers import summarize_notes

__all__ = [
    "PipelineContext",
    "PipelineStep",
    "run_pipeline",
    "summarize_notes",
    "__version__",
]
__version__ = "0.1.0"
