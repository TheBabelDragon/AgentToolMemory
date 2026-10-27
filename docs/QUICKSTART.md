# Quickstart

Requires Python 3.10+.

```bash
git clone https://github.com/TheBabelDragon/AgentToolMemory.git
cd AgentToolMemory
git checkout feat/agent-tool-memory-core

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Tests (no network, no API keys)
pytest

# Demo
python -m examples.horsepowerpoint.demo
# or with persistent memory:
python -m examples.horsepowerpoint.demo --db /tmp/hpp.db --reject-first
python -m examples.horsepowerpoint.demo --db /tmp/hpp.db
```

Inspect memory: SQLite file from `--db`. Audit JSONL from `--audit path.jsonl`.

## Example tool schema

See `engine.set_parameter` in `examples/horsepowerpoint/tools.py`.

## Example authorization denial

Run demo with `--reject-first`; first execute is denied and stored as a `failure` record.
