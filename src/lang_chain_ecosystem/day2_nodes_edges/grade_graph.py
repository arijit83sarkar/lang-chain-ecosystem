from langgraph.graph import StateGraph, START, END
from .grade_state import GradeState

# return {"score": score, "letter": "A", "message": ""}


def callGradeGraph() -> None:
    builder = StateGraph(GradeState)
    builder.add_node("score_to_letter", score_to_letter)
    builder.add_node("add_message", add_message)

    builder.add_edge(START, "score_to_letter")
    builder.add_edge("score_to_letter", "add_message")
    builder.add_edge("add_message", END)
    graph = builder.compile()

    result = graph.invoke({"score": 86, "letter": "", "message": ""})
    print(">>>", result["message"])


def score_to_letter(state: GradeState) -> dict:
    score = state["score"]
    # print(score)
    if score >= 90:
        return {"letter": "A"}
    if score >= 80:
        return {"letter": "B"}
    if score >= 70:
        return {"letter": "C"}
    if score >= 60:
        return {"letter": "D"}
    else:
        return {"letter": "F"}


def add_message(state: GradeState) -> dict:
    letter = state["letter"]
    # print(letter)
    if letter == "A":
        return {"message": "Great, well done!"}
    if letter == "B":
        return {"message": "Good, well done!"}
    else:
        return {"message": "well done!"}
