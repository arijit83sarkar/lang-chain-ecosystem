from typing_extensions import TypedDict


class TriangleState(TypedDict):
    a: float
    b: float
    c: float
    kind: str
