"""
config.py
---------
Loads environment variables from a .env file and exposes them as simple
constants. Import from here instead of calling os.getenv() everywhere.
"""

import os
from dotenv import load_dotenv

# Load .env from the project root (works whether you run from app/ or root)
load_dotenv()

# --- OpenAI ---
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# --- App behaviour ---
MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "1500"))
TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.3"))


def validate_config() -> None:
    """Raise an error early if required settings are missing."""
    if not OPENAI_API_KEY:
        raise EnvironmentError(
            "OPENAI_API_KEY is not set. "
            "Add it to your .env file or export it as an environment variable."
        )
