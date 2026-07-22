from typing_extensions import TypedDict
from typing import Annotated
import operator


class TaglineState(TypedDict):
    topic: str
    tagline: str
    attempts: int
    history: Annotated[list, operator.add]
