"""
llm_service.py
--------------
Thin wrapper around the OpenAI Chat Completions API.

All OpenAI-specific code lives here. If you ever swap providers
(Anthropic, Gemini, etc.) you only need to change this file.
"""

from openai import OpenAI
from app.utils.config import OPENAI_API_KEY, OPENAI_MODEL, MAX_TOKENS, TEMPERATURE


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Send a chat completion request to OpenAI and return the response text.

    Args:
        system_prompt: Instructions that set the LLM's role/behaviour.
        user_prompt:   The actual request from the user.

    Returns:
        The assistant's reply as a plain string.

    Raises:
        EnvironmentError: If the API key is missing.
        openai.OpenAIError: On any API-level failure.
    """
    if not OPENAI_API_KEY:
        raise EnvironmentError(
            "OPENAI_API_KEY is not set. Please add it to your .env file."
        )

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )

    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# Placeholder for local / offline testing (no API key needed)
# ---------------------------------------------------------------------------

PLACEHOLDER_RESPONSE = """
TC-001 | Valid Login with correct credentials
Preconditions: User account exists
Steps: 1. Navigate to login page  2. Enter valid email and password  3. Click Login
Expected: User is redirected to dashboard
Type: Functional

TC-002 | Login with empty password field
Preconditions: User on login page
Steps: 1. Enter valid email  2. Leave password blank  3. Click Login
Expected: Validation error shown — "Password is required"
Type: Negative
""".strip()


def call_llm_placeholder(_system_prompt: str, _user_prompt: str) -> str:
    """Return a hardcoded sample response — useful for UI development without an API key."""
    return PLACEHOLDER_RESPONSE
