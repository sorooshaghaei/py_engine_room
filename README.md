# py_engine_room

A practical "engineering room" for learning and reusing professional Python repo design patterns.

This repository is intentionally generic so you can apply the same structure to almost any project type.

## What you get

- A reusable pipeline architecture: `config -> steps -> artifacts -> logs -> metrics`
- Three templates: `app`, `library`, and `research`
- Runnable demos for each template
- Team workflow docs (Git, PRs, reviews, issues)
- Notebook guidance and hands-on notebooks for active practice
- A project generator script: `tools/new_project.py`

## Quick start

```bash
cd py_engine_room
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
make test
make run
```

## Why this repo exists

The goal is to teach *how to design* repository structures, not to lock you into one layout.

- `PROJECT_STRUCTURE_GUIDE.md` explains how to choose structures for different project goals.
- `PIPELINE_STYLE_GUIDE.md` explains why each pipeline layer exists.
- `templates/` gives copyable starting points.
- `examples/` proves the templates run offline in seconds.

## Suggested learning path

1. Read `PROJECT_STRUCTURE_GUIDE.md`
2. Read `PIPELINE_STYLE_GUIDE.md`
3. Run an example: `python examples/app_demo/main.py --config examples/app_demo/configs/config.yaml`
4. Open notebooks in order under `notebooks/`
5. Create your own repo with `python tools/new_project.py --help`
