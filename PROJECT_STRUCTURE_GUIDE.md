# Project Structure Guide

Use this guide to choose a structure for almost any Python project.

## First principles

Pick structure from constraints:

- How many contributors?
- Is this a one-off script, a reusable package, or a service?
- Will it need tests, CI, release automation, or reproducibility?

As project complexity grows, separate concerns early.

## Recommended baseline

```text
project/
  README.md
  pyproject.toml
  requirements.txt
  src/<package_name>/
  tests/
  configs/
  data/        # gitignored
  outputs/     # gitignored
```

## Why `src/` layout

`src/` layout prevents accidental imports from the repo root and forces installation-like imports during development.

This catches packaging mistakes earlier than flat layouts.

## Why `__init__.py` matters

`__init__.py` marks a directory as a Python package and controls the public API boundary.

Best practice:

- Keep it minimal.
- Avoid side effects at import time.
- Expose only stable public symbols (`__version__`, key functions/classes).

Bad pattern:

- Running file I/O, network calls, or heavy setup in `__init__.py`.

## How to pick between templates

- `templates/app`: CLI/service style; clear entrypoint and orchestration.
- `templates/library`: package-first; importable API is primary.
- `templates/research`: notebook-driven iteration with clean extraction path to `src/`.

## Scaling checklist

- Add lint/format/test automation.
- Add typed interfaces on public modules.
- Add CI checks for `ruff`, `black --check`, `pytest`.
- Add docs for onboarding and team workflow.
- Add release/versioning strategy when public consumers exist.
