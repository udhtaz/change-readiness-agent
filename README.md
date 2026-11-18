# change-readiness-agent

An AI-powered assistant for assessing whether a proposed cloud infrastructure
change is ready to deploy. The project is designed to review synthetic change
requests for approval evidence, deployment and rollback plans, test evidence,
and monitoring readiness while keeping the inference backend replaceable.

## Project goals

- Model a cloud change request with clear, validated data contracts.
- Keep readiness rules and agent orchestration independent of the user interface.
- Support local inference first, with room for MLX, Ollama, vLLM, or hosted
  providers behind the same interface.
- Build toward repeatable evaluations, retrieval, and tool-using workflows in
  later phases.
- Use synthetic examples only so the repository remains safe to share publicly.

## Current status

Phase 1 is a project scaffold. It contains the package boundaries, Pydantic
schema, provider and extension contracts, a minimal Streamlit entry point, and a
smoke test. It intentionally does **not** implement an agent loop, LLM calls,
readiness scoring, assessment rules, retrieval, FastAPI, or deployment
infrastructure yet.

## Architecture

```text
.
├── app.py
├── data/
│   └── synthetic/
│       └── example_change_request.json
├── src/
│   └── change_readiness_agent/
│       ├── agent/
│       │   └── orchestrator.py
│       ├── llm/
│       │   └── provider.py
│       ├── schemas/
│       │   └── change_request.py
│       ├── tools/
│       │   └── base.py
│       └── validation/
│           └── rules.py
├── tests/
│   └── test_smoke.py
└── pyproject.toml
```

- `app.py` is the presentation layer. Business logic belongs in the installed
  package, not in Streamlit.
- `agent` is the future orchestration boundary that will coordinate providers,
  tools, and validation rules.
- `llm` defines the replaceable inference-provider contract without selecting or
  implementing a backend.
- `schemas` contains the Pydantic contracts shared by the UI and future services.
- `tools` and `validation` define extension points; concrete tools and readiness
  rules will be added in later phases.
- `data/synthetic` contains public-safe fixtures used for development and tests.

## Local installation

Requirements:

- Python 3.11 or newer
- macOS, Linux, or Windows
- A local model server is optional during this scaffold phase

Create a virtual environment and install the project in editable mode with its
development dependencies:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1` instead.

Copy the example configuration if you want to prepare local inference settings:

```bash
cp .env.example .env
```

The settings are placeholders and are not consumed by an inference
implementation yet. `.env` is ignored by Git.

## Run the app

```bash
streamlit run app.py
```

Streamlit will print the local browser URL in the terminal. The current screen
only describes the scaffold; it does not submit data to an LLM.

## Run the tests

```bash
pytest
```

The initial smoke test verifies that the package imports and that the bundled
synthetic change request conforms to the Pydantic schema.

## Configuration

`.env.example` documents the planned local LLM connection and inference
settings:

- `LLM_BASE_URL`: OpenAI-compatible endpoint exposed by a local model server.
- `LLM_MODEL_ID`: model identifier understood by that server.
- `LLM_TEMPERATURE`, `LLM_TOP_P`, and `LLM_MAX_TOKENS`: generation controls.
- `LLM_TIMEOUT_SECONDS`: request timeout for a future HTTP provider.

Do not put credentials in `.env.example` or commit a populated `.env` file.

## Synthetic data policy

Only fabricated change requests belong in this repository. Do not add employer
names, internal account or tenant identifiers, proprietary infrastructure
configuration, credentials, or real change-management records. Keep new fixtures
generic and clearly marked as synthetic.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
