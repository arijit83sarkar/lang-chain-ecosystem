from langgraph.graph import StateGraph, START, END
from .tagline_state import TaglineState


def callReducer() -> None:
    builder = StateGraph(TaglineState)
    builder.add_node("draft_tagline", draft_tagline)
    builder.add_node("shorten", shorten)

    builder.add_edge(START, "draft_tagline")
    builder.add_conditional_edges("draft_tagline", check_length, ["shorten", END])
    builder.add_conditional_edges("shorten", check_length, ["shorten", END])

    graph = builder.compile()
    result = graph.invoke(
        {"topic": "Our New Coffe Blend", "tagline": "", "attempts": 0}
    )
    print(">>>", result["tagline"])
    print(f"attempts: {result['attempts']}")
    print(f"history: {result['history']}")


def draft_tagline(state: TaglineState) -> dict:
    tagline = f"{state['topic']}: The Best Choise You Will Make Today!"
    return {"tagline": tagline, "attempts": 0, "history": [tagline]}


def check_length(state: TaglineState) -> str:
    if len(state["tagline"]) <= 40:
        return END
    if state["attempts"] >= 5:
        return END
    return "shorten"


def shorten(state: TaglineState) -> dict:
    words = state["tagline"].split()
    tagline = " ".join(words[:-1])
    return {"tagline": tagline, "attempts": state["attempts"] + 1, "history": [tagline]}
