# nl2sqlp — NL → SQL (project module)

Small rule-based natural-language-to-SQL generator and minimal UI/CLI harness.

## What this folder contains

- `app.py` — Streamlit UI that collects NL queries and shows generated SQL. Maintains conversation history and handles clarifications via `main.nl_to_sql`.
- `main.py` — Orchestrator: loads `schema.json`, runs the pipeline, and implements the clarification protocol using the module-global `pending_intent` variable. Also provides a simple CLI REPL.
- `normaliser.py` — Normalises raw text into a predictable form consumed by the encoder/planner.
- `encoder.py` — Tokenises or maps normalized text into simple tokens used by the planner.
- `planner.py` — Builds a `LogicalForm` (`logical_form.py`) from tokens and `schema.json`. Applies simple heuristics for tables, columns, aggregation and filters.
- `logical_form.py` — Definition of the mutable logical form object (attributes like `tables`, `columns`, `aggregation`, `group_by`, `filters`, `join_required`).
- `clarifier.py` — Encapsulates clarification detection and message generation for ambiguous intents.
- `sql_generator.py` — Converts a populated `LogicalForm` into a SQL string. Uses in-place logical form attributes (e.g., `group_by`, `aggregation`).
- `schema_utils.py` + `schema.json` — Load and represent the canonical schema that drives planner decisions.
- `explain.py`, `lm_adapter.py` — helper modules for explanations and any LM adapter logic; modify only if you understand LM/tokeniser interactions.
- `universal_nl2sql_lm/` — Local model and tokenizer assets (safetensors/tokenizer). Only touch when updating model/tokeniser files.

## Quickstart

Install Streamlit if you want the UI, then run:

```bash
pip install streamlit
streamlit run app.py
```

Or use the CLI REPL to iterate faster:

```bash
python main.py
# then enter natural language queries like: "highest salary department"
```

## Important conventions

- Clarification protocol: `main.py` sets `pending_intent` to a `LogicalForm` when a clarification is required. The next user response is applied to `pending_intent` and then cleared.
- Logical forms are mutated in-place (attributes such as `group_by`, `aggregation`, `join_required`). Follow existing attribute names when changing planner or generator code.
- Schema-driven planning: `planner.py` inspects `schema.json` for table/column matches; update schema and planner together if the data model changes.
- The UI intentionally does not execute generated SQL — it only displays it (see `app.py` footer). Do not add automatic DB execution without explicit safety checks.

## Where to look first when modifying behavior

- Intent recognition & heuristics: `planner.py` and `normaliser.py`.
- Clarification rules: `clarifier.py` and `main.py` (`pending_intent` handling).
- SQL emission: `sql_generator.py`.

If you want, I can also add a `requirements.txt`, a tiny test script that runs a few sample queries through `main.nl_to_sql`, or expand this README with examples and common failure cases — tell me which and I will add them.

