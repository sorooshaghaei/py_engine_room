"""Smoke test for app template pipeline."""

from pathlib import Path

from template_pkg.pipeline import run_pipeline


def test_pipeline_smoke(tmp_path: Path) -> None:
    """Pipeline should create an artifact and metrics."""
    ctx = run_pipeline({"run_name": "smoke", "root_dir": str(tmp_path), "artifact_filename": "out.json"})
    assert "artifact_path" in ctx.artifacts
    assert Path(ctx.artifacts["artifact_path"]).exists()
    assert ctx.metrics["items_written"] == 1.0
