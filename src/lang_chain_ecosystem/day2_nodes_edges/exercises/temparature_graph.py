from langgraph.graph import StateGraph, START, END
from .temparature_state import TemparatureState


def callTemparatureGraph() -> None:
    builder = StateGraph(TemparatureState)

    builder.add_node("f_to_c", f_to_c)
    builder.add_node("c_to_k", c_to_k)

    builder.add_edge(START, "f_to_c")
    builder.add_edge("f_to_c", "c_to_k")
    builder.add_edge("c_to_k", END)

    graph = builder.compile()
    result = graph.invoke({"fahrenheit": 104.8})
    print(">>> Celsius:", result["celsius"])
    print(">>> Kelvin:", result["kelvin"])


def f_to_c(state: TemparatureState) -> dict:
    celsius = (state["fahrenheit"] - 32) * 5 / 9
    return {"celsius": celsius, "kelvin": ""}


def c_to_k(state: TemparatureState) -> dict:
    kelvin = state["celsius"] + 273.15
    return {"kelvin": kelvin}
