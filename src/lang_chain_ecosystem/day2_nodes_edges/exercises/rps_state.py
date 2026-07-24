from typing_extensions import TypedDict


class RPSState(TypedDict):
    player: str
    opponent: str
    outcome: str
