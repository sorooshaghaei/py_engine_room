"""Smoke test for library template pipeline."""

from pathlib import Path

from library_demo_pkg.pipeline import run_pipeline


def test_pipeline_smoke(tmp_path: Path) -> None:
    """Pipeline should create summary and metrics artifacts."""
    config = {
        "run_name": "smoke",
        "root_dir": str(tmp_path),
        "artifact_filename": "summary.json",
        "values": [2, 4, 6],
    }
    ctx = run_pipeline(config)
    assert Path(ctx.artifacts["artifact_path"]).exists()
    assert Path(ctx.artifacts["metrics_path"]).exists()
    assert ctx.metrics["value_mean"] == 4.0
