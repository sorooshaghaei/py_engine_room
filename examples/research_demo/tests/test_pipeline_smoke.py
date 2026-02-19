"""Smoke test for research template pipeline."""

from pathlib import Path

from research_demo_pkg.pipeline import run_pipeline


def test_pipeline_smoke(tmp_path: Path) -> None:
    """Pipeline should create summary and metrics artifacts."""
    config = {
        "run_name": "smoke",
        "root_dir": str(tmp_path),
        "artifact_filename": "notes.md",
        "notes": ["a", "b"],
    }
    ctx = run_pipeline(config)
    assert Path(ctx.artifacts["summary_path"]).exists()
    assert Path(ctx.artifacts["metrics_path"]).exists()
    assert ctx.metrics["note_count"] == 2.0
