"""
test_case_generator.py
----------------------
Orchestrates the full test-case generation pipeline:
  user story → prompt → LLM → raw output

This module is the single place that wires prompts and the LLM service
together. The Streamlit UI (main.py) calls generate() and gets back text.
"""

from app.prompts.test_case_prompt import SYSTEM_PROMPT, build_user_prompt
from app.services.llm_service import call_llm, call_llm_placeholder


def generate(user_story: str, use_placeholder: bool = False) -> str:
    """
    Generate test cases for a given user story.

    Args:
        user_story:       The requirement or user story text.
        use_placeholder:  If True, skip the real API call and return sample
                          output. Handy during UI development.

    Returns:
        Raw test case text produced by the LLM (or the placeholder).
    """
    if not user_story.strip():
        raise ValueError("User story cannot be empty.")

    system_prompt = SYSTEM_PROMPT
    user_prompt = build_user_prompt(user_story)

    if use_placeholder:
        return call_llm_placeholder(system_prompt, user_prompt)

    return call_llm(system_prompt, user_prompt)
