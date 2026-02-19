"""Basic import tests for template package."""

from template_pkg import __version__, run_pipeline, summarize_values


def test_import_package() -> None:
    """Package exports should be available."""
    assert __version__
    assert callable(run_pipeline)
    assert summarize_values([1.0, 3.0])["mean"] == 2.0
