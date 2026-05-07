# AI Test Case Generator

AI-assisted test case generation tool for QA and automation workflows.

This project explores how LLMs can help improve engineering productivity by generating:
- Functional test cases
- Edge cases
- Negative scenarios
- Robot Framework templates

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

## 🛠 Tech Stack

### Core
- Python
- Streamlit
- FastAPI

### AI
- OpenAI API
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
