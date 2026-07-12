.PHONY: sync validate test lint security benchmark all

sync:
	python scripts/sync_skill_assets.py

validate: sync
	python scripts/validate_all.py

test: sync
	python -m pytest

lint:
	ruff check .
	ruff format --check .

security:
	bandit -q -r src scripts

benchmark: sync
	python scripts/run_benchmarks.py benchmarks/cases benchmarks/predictions/example_predictions.jsonl

all: validate test lint security benchmark
