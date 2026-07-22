from langgraph.graph import StateGraph, START, END
from .tagline_state import TaglineState


def callCycleEdges() -> None:
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


def draft_tagline(state: TaglineState) -> dict:
    return {
        "tagline": f"{state['topic']}: The Best Choise You Will Make Today!",
        "attempts": 0,
    }


def check_length(state: TaglineState) -> str:
    if len(state["tagline"]) <= 40:
        return END
    if state["attempts"] >= 5:
        return END
    return "shorten"


def shorten(state: TaglineState) -> dict:
    words = state["tagline"].split()
    return {"tagline": " ".join(words[:-1]), "attempts": state["attempts"] + 1}
