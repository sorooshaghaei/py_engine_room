PYTHON ?= python

.PHONY: setup test lint format run run-library run-research

setup:
	$(PYTHON) -m pip install -r requirements-dev.txt

test:
	pytest

lint:
	ruff check .

format:
	black .
	ruff check --fix .

run:
	PYTHONPATH=examples/app_demo/src $(PYTHON) examples/app_demo/main.py --config examples/app_demo/configs/config.yaml

run-library:
	PYTHONPATH=examples/library_demo/src $(PYTHON) examples/library_demo/main.py --config examples/library_demo/configs/config.yaml

run-research:
	PYTHONPATH=examples/research_demo/src $(PYTHON) examples/research_demo/main.py --config examples/research_demo/configs/config.yaml
