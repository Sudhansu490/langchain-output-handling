# LangChain Output Handling

Hands-on demos of LangChain output handling — OutputParsers (Str, JSON, Pydantic, Structured) vs `with_structured_output` (TypedDict / Pydantic / JSON).

> Repo: `https://github.com/Sudhansu490/langchain-output-handling`

## Overview

LangChain offers two main ways to get structured data out of LLMs:

1. **Output Parsers** — classic `PromptTemplate | Model | Parser` chaining
2. **Structured Output** — `model.with_structured_output(schema)` with enforced schemas (Pydantic / TypedDict / JSON Schema)

This repo compares both approaches with runnable examples using **OpenAI** and **HuggingFace** models.

## Project Structure

```
LangChain Output Handling/
├── langchain-output-parsers/          # Classic parser chain examples
│   ├── stroutputparser.py             # Prompt chaining without parser
│   ├── stroutputparser1.py            # StrOutputParser in chain: template | model | parser
│   ├── jsonoutputparser.py            # JsonOutputParser + format instructions
│   ├── pydanticoutputparser.py        # PydanticOutputParser with validation
│   └── structuredoutputparser.py      # StructuredOutputParser via ResponseSchema
│
├── langchain-structured-output/       # model.with_structured_output examples
│   ├── with_structured_output_pydantic.py   # Pydantic BaseModel schema
│   ├── with_structured_output_typeddict.py  # TypedDict + Annotated
│   ├── with_structured_output_json.py       # Raw JSON Schema
│   ├── with_structured_output_llama.py      # TinyLlama via HuggingFace
│   ├── pydantic_demo.py                     # Pydantic validation basics
│   ├── typeddict_demo.py                    # TypedDict basics
│   ├── json_schema.json                     # Example student schema
│   └── students_dataset.csv                 # (placeholder dataset)
│
├── .gitignore
└── README.md
```

## Examples

### 1. Output Parsers

| File | Parser | Model | Description |
|------|--------|-------|-------------|
| `stroutputparser.py` | — | `google/gemma-2-2b-it` | Two-step chain: detailed report → 5-line summary via manual `invoke` |
| `stroutputparser1.py` | `StrOutputParser` | `ChatOpenAI` | Idiomatic chain: `template1 | model | parser | template2 | model | parser` |
| `jsonoutputparser.py` | `JsonOutputParser` | `google/gemma-2-2b-it` | `get_format_instructions()` injected into prompt |
| `pydanticoutputparser.py` | `PydanticOutputParser` | `google/gemma-2-2b-it` | Validates against `Person(name, age>18, city)` |
| `structuredoutputparser.py` | `StructuredOutputParser` | `google/gemma-2-2b-it` | `ResponseSchema` for `fact_1, fact_2, fact_3` |

### 2. Structured Output

| File | Schema Type | Model | Description |
|------|-------------|-------|-------------|
| `with_structured_output_pydantic.py` | `Pydantic BaseModel` | `ChatOpenAI` | `Review` with `key_themes, summary, sentiment, pros, cons, name` |
| `with_structured_output_typeddict.py` | `TypedDict` | `ChatOpenAI` | Same `Review` using `Annotated[Literal["pos","neg"]]` |
| `with_structured_output_json.py` | `JSON Schema` | `ChatOpenAI` | Raw JSON schema with `required: [key_themes, summary, sentiment]` |
| `with_structured_output_llama.py` | `Pydantic` | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | Same schema on open model |

Supporting demos: `pydantic_demo.py` (validation + `model_dump_json()`), `typeddict_demo.py` (type hints).

## Setup

```bash
# 1. Clone
git clone https://github.com/Sudhansu490/langchain-output-handling.git
cd langchain-output-handling

# 2. Create venv (Python 3.10+)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install deps
pip install langchain langchain-openai langchain-huggingface python-dotenv pydantic

# Or if requirements.txt is present
pip install -r requirements.txt

# 4. Env
cp .env.example .env  # add OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN
```

`.env` example:
```
OPENAI_API_KEY=sk-...
HUGGINGFACEHUB_API_TOKEN=hf_...
```

## Usage

```bash
# Output parsers
python langchain-output-parsers/stroutputparser1.py
python langchain-output-parsers/jsonoutputparser.py
python langchain-output-parsers/pydanticoutputparser.py
python langchain-output-parsers/structuredoutputparser.py

# Structured output
python langchain-structured-output/with_structured_output_pydantic.py
python langchain-structured-output/with_structured_output_typeddict.py
python langchain-structured-output/with_structured_output_json.py
python langchain-structured-output/with_structured_output_llama.py

# Basics
python langchain-structured-output/pydantic_demo.py
python langchain-structured-output/typeddict_demo.py
```

## Key Learnings

*   `StrOutputParser` is simplest for text chaining.
*   `JsonOutputParser` fails if output is not valid JSON — needs prompt hardening.
*   `PydanticOutputParser` validates but still prompt-dependent.
*   `StructuredOutputParser` does NOT validate against schema automatically.
*   `with_structured_output` enforces schema at model level — more reliable for production.

## Tech Stack

`LangChain` · `LangChain-OpenAI` · `LangChain-HuggingFace` · `Pydantic` · `Python`

## License

MIT
