"""
config.py
---------
Loads environment variables from a .env file and exposes them as simple
constants. Import from here instead of calling os.getenv() everywhere.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# --- OpenAI ---
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# --- Anthropic ---
ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
ANTHROPIC_MODEL: str = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")

# --- Google Gemini ---
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# --- App behaviour ---
MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "1500"))
TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.3"))


def validate_config(provider: str) -> None:
    """Raise an error early if the required API key for the chosen provider is missing."""
    if provider == "openai" and not OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY is not set. Add it to your .env file.")
    if provider == "anthropic" and not ANTHROPIC_API_KEY:
        raise EnvironmentError("ANTHROPIC_API_KEY is not set. Add it to your .env file.")
    if provider == "gemini" and not GEMINI_API_KEY:
        raise EnvironmentError("GEMINI_API_KEY is not set. Add it to your .env file.")
