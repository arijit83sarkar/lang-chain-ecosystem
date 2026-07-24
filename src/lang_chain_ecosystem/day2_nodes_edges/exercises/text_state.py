from typing_extensions import TypedDict


class TextState(TypedDict):
    raw: str
    cleaned: str
    word_count: int
