# Langchain-Learning-Modules-CampusX

A **structured, hands-on learning repository** covering the full LangChain ecosystem — from models and prompts to RAG, tools, runnables, and agents — aligned with **modern LangChain (LCEL-first)** practices.

This repo is designed for:
- Step-by-step learning
- Practical experimentation
- Clear mental models of LangChain internals

---

## Repository Structure

```
Langchain-Learning-Modules-CampusX
│
├── 1_models                # LLMs, Chat Models, Embeddings
├── 2_prompts               # Prompt templates (single & multi-message)
├── 3_output                # Structured outputs & output parsers
├── 4_chains                # Chains & LCEL Runnables
├── 5_rag                   # RAG pipeline (loaders → splitters → retrievers)
├── 6_tools                 # Built-in tools, custom tools, tool flows
├── 7_agents                # Agent-based workflows
│
├── requirements.txt
├── requirements-lock.txt
├── Notes.md
├── README.md
└── LICENSE
```

---

## Models

### Language Models
- LLMs vs Chat Models
- OpenAI, Anthropic, Google, HuggingFace (API + local)

```
1_models/
├── 1_language_models/
│   ├── 1_llm/
│   └── 2_chat_models/
└── 2_embedding_models/
```

Covers:
- Model invocation
- Chat-based interfaces
- Embedding generation
- Document similarity

---

## Prompts

Covers **prompt engineering fundamentals** and LangChain abstractions:

```
2_prompts/
├── 1_single_message/
│   ├── static_prompts
│   └── dynamic_prompts
└── 2_multi_message/
    ├── static_prompts
    └── dynamic_prompts
```

Includes:
- `PromptTemplate`
- `ChatPromptTemplate`
- `MessagePlaceholder`
- Dynamic prompt generation

---

## Output Handling

### Structured Output
- TypedDict
- Pydantic
- JSON Schema

### Output Parsers
- String
- JSON
- Pydantic

```
3_output/
├── 1_Structured_output/
└── 2_Output_parsers/
```

Focuses on **schema-safe LLM outputs**, a production-critical skill.

---

## Chains & Runnables (LCEL)

Covers both **legacy chains** and **modern LCEL runnables**:

```
4_chains/
├── 1_chains/
└── 2_runnables/
```

Includes:
- Sequential & parallel chains
- `RunnableSequence`
- `RunnableParallel`
- `RunnableLambda`
- `RunnablePassthrough`
- `RunnableBranch`

---

## RAG (Retrieval-Augmented Generation)

End-to-end RAG pipeline:

```
5_rag/
├── 1_document_loaders/
├── 2_text_splitters/
├── 3_vector_store/
├── 4_retreivers/
└── 5_rag/
```

Covered topics:
- Text, PDF, CSV, web loaders
- Recursive & semantic splitters
- Chroma vector store
- Retriever strategies:
  - Source-based
  - MMR
  - Multi-query
  - Context compression
- Complete RAG notebooks

---

## Tools

```
6_tools/
├── 1_built_in_tools
├── 2_custom_tools
├── 3_toolkits
└── 4_tool_flow
```

Covers:
- Built-in tools (search, shell)
- Custom tools using `@tool`
- Structured tools
- Tool orchestration & flows

---

## Agents

```
7_agents/
└── basic_ddg_search+weater_agent.ipynb
```

Introduces:
- Agent reasoning
- Tool calling
- Search + external API integration

---

## Environment & Versioning (Important)

LangChain is fast-moving and highly version-sensitive.

Recommended setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---
