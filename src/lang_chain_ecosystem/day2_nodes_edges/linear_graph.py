from langgraph.graph import StateGraph, START, END
from .tagline_state import TaglineState


def callLinearGraph() -> None:
    builder = StateGraph(TaglineState)
    builder.add_node("draft_tagline", draft_tagline)
    builder.add_node("shout_it", shout_it)

    builder.add_edge(START, "draft_tagline")
    builder.add_edge("draft_tagline", "shout_it")
    builder.add_edge("shout_it", END)

    graph = builder.compile()

    result = graph.invoke({"topic": "Our New Coffee Blend", "tagline": ""})
    print(">>>", result["tagline"])


def callConditionalEdges() -> None:
    builder = StateGraph(TaglineState)
    builder.add_node("draft_tagline", draft_tagline)
    builder.add_node("shout_it", shout_it)
    builder.add_node("trim_it", trim_it)

    builder.add_edge(START, "draft_tagline")
    builder.add_edge("draft_tagline", "shout_it")
    builder.add_conditional_edges("shout_it", check_length, ["trim_it", END])
    builder.add_edge("trim_it", END)

    graph = builder.compile()
    result = graph.invoke({"topic": "Our New Coffee Blend", "tagline": ""})
    print(">>>", result["tagline"])

    result = graph.invoke({"topic": "Fresh", "tagline": ""})
    print(">>>", result["tagline"])


def shout_it(state: TaglineState) -> dict:
    return {"tagline": f"{state['tagline'].upper()}"}


def draft_tagline(state: TaglineState) -> dict:
    return {"tagline": f"{state['topic']}: Now better than ever!"}


def check_length(state: TaglineState) -> str:
    if len(state["tagline"]) > 40:
        return "trim_it"
    return END


def trim_it(state: TaglineState) -> dict:
    return {"tagline": state["tagline"][:40].rstrip() + "..."}
