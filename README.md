# AI Test Case Generator

AI-assisted test case generation tool for QA and automation workflows.

This project explores how LLMs can help improve engineering productivity by generating:
- Functional test cases
- Edge cases
- Negative scenarios
- Robot Framework templates

---

## 🤖 What It Does

1. **Paste a user story or requirement** into the web UI
2. **Choose your AI provider** from the sidebar — OpenAI, Anthropic Claude, or Google Gemini
3. **AI generates structured test cases** — acting as a senior QA engineer — covering:
   - Functional (happy path) scenarios
   - Edge cases
   - Negative / failure scenarios
4. **Each test case includes:** ID, title, preconditions, steps, expected result, and type
5. **Export in two formats:**
   - Plain `.txt` for documentation or review
   - `.robot` file skeleton ready for Robot Framework + SeleniumLibrary

> A **placeholder mode** is available in the sidebar — returns sample output with no API key needed, useful for UI testing.

---

## 🗂 Key Files

| File | Role |
|---|---|
| `app/main.py` | Streamlit UI — form, tabs, download buttons |
| `app/generators/test_case_generator.py` | Orchestrator — wires prompt + LLM together |
| `app/prompts/test_case_prompt.py` | Prompt templates for the LLM |
| `app/services/llm_service.py` | Multi-provider LLM router — OpenAI, Anthropic, Gemini |
| `app/formatters/robot_formatter.py` | Converts raw output into `.robot` file format |
| `app/utils/config.py` | Loads env vars for all providers (API keys, models, tokens, temperature) |

---

## 🚀 Goals

### Input
- User stories
- Requirements
- API specifications

### Output
- Functional test cases
- Edge cases
- Negative test scenarios
- Robot Framework templates

---

## 🏗 High-Level Workflow

```text
Requirement / User Story
        ↓
LLM Processing
        ↓
Generate:
- Functional Test Cases
- Edge Cases
- Negative Scenarios
        ↓
Export to Robot Framework Template
```
---

# 📦 Project Structure

```
ai-test-case-generator/
├── app/
│   ├── formatters/
│   │   └── robot_formatter.py   # Converts LLM output to .robot file format
│   ├── generators/
│   │   └── test_case_generator.py  # Orchestrates prompt → LLM → output pipeline
│   ├── prompts/
│   │   └── test_case_prompt.py  # System & user prompt templates
│   ├── services/
│   │   └── llm_service.py       # Multi-provider LLM router (OpenAI, Anthropic, Gemini)
│   ├── utils/
│   │   └── config.py            # Loads env vars and exposes config constants
│   └── main.py                  # Streamlit UI entry point
├── .env.example                 # Example environment variables
├── .gitignore
└── requirements.txt
```

---
# 🚀 Setup & Run

## 1. Create Virtual Environment

```bash
python -m venv venv
```

This only needs to be done once.

---

## 2. Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Streamlit App

```bash
streamlit run app/main.py
```

---

## 5. Open in Browser

```text
http://localhost:8501
```

---

## ✨ Example

### Input
```text
User can transfer money between accounts
```

### Generated Ideas
- Valid transfer
- Insufficient balance
- Invalid destination account
- Concurrent transfer attempts
- Network timeout during transaction

---

## ⚙️ AI Configuration

Three AI providers are built in and selectable from the sidebar dropdown — no code changes needed.

### Setup

Copy `.env.example` to `.env` and fill in the key(s) for the provider(s) you want to use:

```bash
cp .env.example .env
```

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | Any OpenAI chat model |
| `ANTHROPIC_API_KEY` | — | Anthropic API key |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-6` | Any Claude model |
| `GEMINI_API_KEY` | — | Google AI Studio API key |
| `GEMINI_MODEL` | `gemini-2.0-flash` | Any Gemini model |
| `MAX_TOKENS` | `1500` | Max tokens in the LLM response |
| `TEMPERATURE` | `0.3` | Lower = more deterministic output |

Only set the key(s) for the provider you plan to use. The others can be left blank.

---

### 🟠 OpenAI

| Model | Best for |
|---|---|
| `gpt-4o` | Most capable |
| `gpt-4o-mini` | Balanced — speed + cost (default) |
| `gpt-4-turbo` | Long-context tasks |

---

### 🟣 Anthropic Claude

| Model | Best for |
|---|---|
| `claude-opus-4-7` | Most capable, complex reasoning |
| `claude-sonnet-4-6` | Balanced — speed + quality (default) |
| `claude-haiku-4-5-20251001` | Fastest, lowest cost |

---

### 🔵 Google Gemini

| Model | Best for |
|---|---|
| `gemini-2.0-flash` | Fast, cost-efficient (default) |
| `gemini-1.5-pro` | Complex, long-context tasks |
| `gemini-1.5-flash` | Lightweight, low latency |

---

## 🛠 Tech Stack

### Core
- Python
- Streamlit
- FastAPI

### AI
- OpenAI API (`gpt-4o-mini`)
- Anthropic Claude (`claude-sonnet-4-6`)
- Google Gemini (`gemini-2.0-flash`)
- Prompt Engineering

### QA / Automation
- Robot Framework
- API Testing

---

## 📌 Current Status

Active exploration and prototype development.

---

## 📂 Planned Features

- Requirement → Test Case generation
- Edge case suggestions
- Negative test generation
- Robot Framework export
- API testing templates
- AI-generated bug reproduction ideas

---

## 💡 Vision

Exploring how AI can augment enterprise QA workflows and modern engineering practices.

---

## 👩‍💻 Author

Bee Romphan

Senior enterprise SDET exploring AI-assisted engineering workflows.
