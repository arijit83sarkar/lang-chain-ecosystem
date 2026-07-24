from langgraph.graph import StateGraph, START, END
from .text_state import TextState
import string


def callTextNormalizerGraph() -> None:
    builder = StateGraph(TextState)
    builder.add_node("strip_and_lower", strip_and_lower)
    builder.add_node("remove_punctuation", remove_punctuation)
    builder.add_node("count_words", count_words)

    builder.add_edge(START, "strip_and_lower")
    builder.add_edge("strip_and_lower", "remove_punctuation")
    builder.add_edge("remove_punctuation", "count_words")
    builder.add_edge("count_words", END)

    graph = builder.compile()
    result = graph.invoke(
        {"raw": "  Hello, World! This IS a Test.  ", "cleaned": "", "word_count": ""}
    )
    print(">>>", result["cleaned"])


def strip_and_lower(state: TextState) -> dict:
    cleaned = str(state["raw"]).replace(" ", "").lower()
    return {"cleaned": cleaned}


def remove_punctuation(state: TextState) -> dict:
    cleaned = state["cleaned"].translate(string.punctuation)
    return {"cleaned": cleaned}


def count_words(state: TextState) -> dict:
    count = len(state["cleaned"])
    return {"count": count}
