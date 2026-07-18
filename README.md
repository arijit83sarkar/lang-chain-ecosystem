# lang-chain-ecosystem

Empty starter project for building with the LangChain ecosystem, managed with `uv`.

## Included packages

- `langchain` — high-level chains, agents, and orchestration
- `langchain-core` — base abstractions (messages, runnables, prompts)
- `langchain-community` — third-party integrations (vector stores, loaders, tools)
- `langchain-openai` — OpenAI-compatible chat/embeddings models (also works with
  OpenRouter by pointing `base_url` at `https://openrouter.ai/api/v1`)

## Setup

```bash
uv sync
cp .env.example .env   # fill in whichever key(s) you need
uv run lang-chain-ecosystem
```

## Adding more packages

```bash
uv add langchain-anthropic      # Anthropic models
uv add langgraph                # already pulled in as a langchain dependency
uv add langchain-chroma          # e.g. a vector store
```

## Layout

```
lang-chain-ecosystem/
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env.example
├── README.md
└── src/
    └── lang_chain_ecosystem/
        └── __init__.py    # entry point, currently a hello-world main()
```
