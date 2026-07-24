from langgraph.graph import StateGraph, START, END
from .password_state import PassowrdState
import re


def callPasswordGraph() -> None:
    builder = StateGraph(PassowrdState)

    builder.add_node("route_length", route_length)
    builder.add_node("too_short", too_short)
    builder.add_node("check_complexity", check_complexity)
    builder.add_node("route_complexity", route_complexity)
    builder.add_node("strong", strong)
    builder.add_node("weak", weak)

    builder.add_conditional_edges(
        START, route_length, ["too_short", "check_complexity"]
    )
    builder.add_conditional_edges(
        "check_complexity", route_complexity, ["strong", "weak"]
    )
    builder.add_edge("too_short", END)
    builder.add_edge("strong", END)
    builder.add_edge("weak", END)

    graph = builder.compile()
    result = graph.invoke({"password": "Alllowercase1"})
    print(">>>", result["verdict"])


def route_length(state: PassowrdState) -> str:
    if len(state["password"]) <= 8:
        return "too_short"
    else:
        return "check_complexity"


def too_short(state: PassowrdState) -> dict:
    return {"verdict": "Too short (needs 8+ characters)"}


def check_complexity(state: PassowrdState) -> dict:
    return {}


def route_complexity(state: PassowrdState) -> str:
    password = state["password"]

    # has_upper = any(password.isupper() for char in password)
    # has_lower = any(password.islower() for char in password)
    # has_digit = any(password.isdigit() for char in password)

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"

    if bool(re.match(pattern, password)):
        return "strong"
    else:
        return "weak"


def strong(state: PassowrdState) -> str:
    return {"verdict": "Strong"}


def weak(state: PassowrdState) -> str:
    return {"verdict": "Weak (needs a mix of upper/lower/digits)"}
