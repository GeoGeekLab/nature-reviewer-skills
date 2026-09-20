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
	python scripts/validate_benchmark_suite.py benchmarks/controlled_v1/cases.jsonl
	python scripts/run_benchmarks.py benchmarks/controlled_v1/cases.jsonl benchmarks/controlled_v1/oracle_predictions.jsonl

all: validate test lint security benchmark
