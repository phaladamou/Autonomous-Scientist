# Contributing to Autonomous-Scientist

Thanks for your interest in contributing!

## Repository layout

The project is organized by scientific-workflow concern:

- `apps/` — user-facing applications (web, dashboard, cli)
- `scientist/` — the autonomous research loop (orchestrator, planning, decisions)
- `hypothesis/` — hypothesis generation, ranking, prediction, falsification, validation
- `literature/` — connectors, search, retrieval, parsing, evidence, gap detection
- `experiment/` — design, protocols, execution, reproducibility
- `simulation/` — engines, environments, scenarios, sandbox
- `analysis/` — statistics, metrics, visualization, uncertainty, robustness
- `memory/` — working, episodic, semantic memory and retrieval
- `learning/` — feedback loops and learned policies
- `models/` — language, scientific, and surrogate models
- `runtime/` — engine, workflows, scheduler, state, checkpoints, budgets
- `evaluation/` — benchmarks, datasets, baselines, reports
- `interfaces/` — API, SDK, protocols
- `storage/` — database, artifacts, datasets, provenance
- `security/` — permissions, sandbox policy, audit
- `packages/` — shared types, schemas, configuration, utilities
- `tests/` — unit, integration, end-to-end tests and fixtures
- `infra/` — docker, deployment, observability
- `docs/` — architecture and scientific-method documentation
- `examples/` — runnable example projects
- `scripts/` — developer and CI scripts

## Development

1. Use Python 3.12+.
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
3. Install the project: `pip install -e .`
4. Run tests: `pytest` (configuration lives in `pytest.ini`)

## Guidelines

- Add new code to the module directory that matches its concern.
- Keep public interfaces documented in `docs/`.
- Add or update tests alongside every behavior change.
- Never commit secrets, credentials, or API keys.
