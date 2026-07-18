"""Configuration loading for north-mini-chat."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

MODEL_ID = "cohere/north-mini-code:free"
BASE_URL = "https://openrouter.ai/api/v1"


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str = MODEL_ID
    base_url: str = BASE_URL


def load_settings() -> Settings:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Add it to a .env file or export "
            "it in your shell before running north-chat."
        )
    return Settings(api_key=api_key)
