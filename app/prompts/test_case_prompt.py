"""
test_case_prompt.py
-------------------
Prompt templates for test case generation.

Keeping prompts in their own module makes them easy to iterate on
without touching any business logic.
"""


SYSTEM_PROMPT = """
You are a senior QA engineer and test design expert.
Your job is to generate thorough, well-structured test cases from a given
user story or requirement.

For each test case include:
- Test Case ID  (e.g. TC-001)
- Title
- Preconditions
- Steps
- Expected Result
- Type  (Functional / Edge Case / Negative)

Be concise but precise. Use plain English. Do not add markdown headers.
""".strip()


def build_user_prompt(user_story: str) -> str:
    """
    Slot a user story into the generation prompt.

    Args:
        user_story: The requirement or user story text provided by the user.

    Returns:
        A formatted prompt string ready to send to the LLM.
    """
    return f"""
Generate test cases for the following user story:

---
{user_story.strip()}
---

Include at minimum:
- 2 functional (happy path) test cases
- 2 edge case test cases
- 2 negative / failure test cases
""".strip()
