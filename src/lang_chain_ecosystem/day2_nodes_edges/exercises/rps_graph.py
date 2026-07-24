from langgraph.graph import StateGraph, START, END
from .rps_state import RPSState


def callRPSGraph() -> None:
    builder = StateGraph(RPSState)

    builder.add_node("decide", decide)
    builder.add_node("win", win)
    builder.add_node("lose", lose)
    builder.add_node("tie", tie)

    builder.add_conditional_edges(START, decide, ["win", "lose", "tie"])
    builder.add_edge("win", END)
    builder.add_edge("lose", END)
    builder.add_edge("tie", END)

    graph = builder.compile()
    result = graph.invoke({"player": "scissors", "opponent": "rock"})
    print(">>>", result["outcome"])


def decide(state: RPSState) -> str:
    player = state["player"]
    opponent = state["opponent"]

    if player == opponent:
        return "tie"
    elif (
        (player == "rock" and opponent == "scissors")
        or (player == "paper" and opponent == "rock")
        or (player == "scissors" and opponent == "paper")
    ):
        return "win"
    else:
        return "lose"


def win(state: RPSState) -> dict:
    return {"outcome": "You win!"}


def lose(state: RPSState) -> dict:
    return {"outcome": "You lose."}


def tie(state: RPSState) -> dict:
    return {"outcome": "Tie."}
