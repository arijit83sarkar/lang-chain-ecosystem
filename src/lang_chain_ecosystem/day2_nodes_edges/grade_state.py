from typing_extensions import TypedDict


class GradeState(TypedDict):
    score: int
    letter: str
    message: str
