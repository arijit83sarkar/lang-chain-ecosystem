"""Thin wrapper around the OpenRouter-backed ChatOpenAI client."""

from langchain_openai import ChatOpenAI
from dataclasses import dataclass
from .config import load_settings


@dataclass(frozen=True)
class MyChatOpenAI:
    chatOpenAI: ChatOpenAI


def loadChatOpenAI() -> ChatOpenAI:
    settings = load_settings()
    return ChatOpenAI(
        model=settings.model,
        base_url=settings.base_url,
        api_key=settings.api_key,
        default_headers={"HTTP-Referer": "https://local-dev"},
    )
    # return MyChatOpenAI(chatOpenAI=chatOpenAI)
