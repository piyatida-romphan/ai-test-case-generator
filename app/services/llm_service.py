"""
llm_service.py
--------------
LLM provider implementations. Each provider has its own function.
call_llm() routes to the correct one based on the provider argument.

To add a new provider: add a _call_<provider>() function and a branch in call_llm().
"""

from app.utils.config import (
    OPENAI_API_KEY, OPENAI_MODEL,
    ANTHROPIC_API_KEY, ANTHROPIC_MODEL,
    GEMINI_API_KEY, GEMINI_MODEL,
    MAX_TOKENS, TEMPERATURE,
)


# ---------------------------------------------------------------------------
# OpenAI
# ---------------------------------------------------------------------------

def _call_openai(system_prompt: str, user_prompt: str) -> str:
    from openai import OpenAI
    if not OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY is not set. Please add it to your .env file.")
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
# Anthropic Claude
# ---------------------------------------------------------------------------

def _call_anthropic(system_prompt: str, user_prompt: str) -> str:
    import anthropic
    if not ANTHROPIC_API_KEY:
        raise EnvironmentError("ANTHROPIC_API_KEY is not set. Please add it to your .env file.")
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    message = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return message.content[0].text.strip()


# ---------------------------------------------------------------------------
# Google Gemini
# ---------------------------------------------------------------------------

def _call_gemini(system_prompt: str, user_prompt: str) -> str:
    import google.generativeai as genai
    if not GEMINI_API_KEY:
        raise EnvironmentError("GEMINI_API_KEY is not set. Please add it to your .env file.")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=system_prompt,
    )
    response = model.generate_content(user_prompt)
    return response.text.strip()


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

def call_llm(system_prompt: str, user_prompt: str, provider: str = "openai") -> str:
    """
    Route to the correct LLM provider.

    Args:
        system_prompt: Instructions that set the LLM's role/behaviour.
        user_prompt:   The actual request from the user.
        provider:      One of "openai", "anthropic", "gemini".

    Returns:
        The assistant's reply as a plain string.
    """
    if provider == "openai":
        return _call_openai(system_prompt, user_prompt)
    if provider == "anthropic":
        return _call_anthropic(system_prompt, user_prompt)
    if provider == "gemini":
        return _call_gemini(system_prompt, user_prompt)
    raise ValueError(f"Unknown provider '{provider}'. Choose from: openai, anthropic, gemini.")


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
