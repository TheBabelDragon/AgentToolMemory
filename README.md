# AgentToolMemory

Reusable, **model-agnostic** agent capability layer:

- **Typed tools** — schemas, semantic versions, discovery, structured results
- **Structured memory** — facts, events, decisions, outcomes, failures (SQLite)
- **Enforceable permissions** — READ / PROPOSE / EXECUTE with an explicit authorize boundary
- **Auditable lifecycle** — DISCOVER → READ → RECALL → PROPOSE → VALIDATE → AUTHORIZE → EXECUTE → OBSERVE → RECORD

HorsePowerPoint is the first **demonstration adapter** (simulated ECU tuning). The core has no automotive dependencies.

## Install

```bash
pip install -e ".[dev]"
```

## Test

```bash
pytest
```

## Demo

```bash
python -m examples.horsepowerpoint.demo
python -m examples.horsepowerpoint.demo --db /tmp/hpp.db --reject-first
```

## Layout

```
src/agent_tool_memory/
  registry/     tool registration, schemas, discovery
  memory/       records, SQLite backend
  execution/    lifecycle, authorization, audit
  adapters/     protocol integrations (reserved)
examples/horsepowerpoint/
tests/
docs/
```

See [docs/QUICKSTART.md](docs/QUICKSTART.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/SECURITY.md](docs/SECURITY.md).

## License

MIT
