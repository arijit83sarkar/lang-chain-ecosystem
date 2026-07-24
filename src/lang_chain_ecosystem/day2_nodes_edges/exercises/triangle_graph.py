from langgraph.graph import StateGraph, START, END
from .triangle_state import TriangleState


def callTriangleGraph() -> None:
    builder = StateGraph(TriangleState)

    builder.add_node("classify", classify)
    builder.add_node("invalid", invalid)
    builder.add_node("equilateral", equilateral)
    builder.add_node("isoscales", isoscales)
    builder.add_node("scalene", scalene)

    builder.add_conditional_edges(
        START, classify, ["invalid", "equilateral", "isoscales", "scalene"]
    )
    builder.add_edge("invalid", END)
    builder.add_edge("equilateral", END)
    builder.add_edge("isoscales", END)
    builder.add_edge("scalene", END)

    graph = builder.compile()
    result = graph.invoke({"a": 4, "b": 9, "c": 7})
    print(">>>", result["kind"])


def classify(state: TriangleState) -> str:
    a = state["a"]
    b = state["b"]
    c = state["c"]

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or c == a:
            return "isoscales"
        else:
            return "scalene"
    else:
        return "invalid"


def invalid(state: TriangleState) -> dict:
    return {"kind": "Not a valid triangle."}


def equilateral(state: TriangleState) -> dict:
    return {"kind": "Equilateral."}


def isoscales(state: TriangleState) -> dict:
    return {"kind": "Isoscales."}


def scalene(state: TriangleState) -> dict:
    return {"kind": "Scalene."}
