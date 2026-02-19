"""Basic import tests for template package."""

from research_demo_pkg import __version__, run_pipeline, summarize_notes


def test_import_package() -> None:
    """Package exports should be available."""
    assert __version__
    assert callable(run_pipeline)
    assert "Research Summary" in summarize_notes(["x"])
