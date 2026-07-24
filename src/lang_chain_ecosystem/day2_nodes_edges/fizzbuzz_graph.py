from langgraph.graph import StateGraph, START, END
from .fizz_state import FizzState

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


def callFizzBuzzGraph() -> None:
    builder = StateGraph(FizzState)
    builder.add_node("fizzbuzz", fizzbuzz)
    builder.add_node("buzz", buzz)
    builder.add_node("fizz", fizz)
    builder.add_node("number", number)

    builder.add_conditional_edges(START, route, ["fizzbuzz", "buzz", "fizz", "number"])
    builder.add_edge("fizzbuzz", END)
    builder.add_edge("buzz", END)
    builder.add_edge("fizz", END)
    builder.add_edge("number", END)

    graph = builder.compile()

    for n in [15, 9, 10, 7,6,30]:
        result = graph.invoke({"n": n, "result": ""})
        print(n, "->", result["result"])


def route(state: FizzState) -> str:
    if state["n"] % 15 == 0:
        return "fizzbuzz"
    if state["n"] % 5 == 0:
        return "buzz"
    if state["n"] % 3 == 0:
        return "fizz"
    return "number"


def fizzbuzz(state: FizzState) -> dict:
    return {"result": "FizzBuzz"}


def buzz(state: FizzState) -> dict:
    return {"result": "Buzz"}


def fizz(state: FizzState) -> dict:
    return {"result": "Fizz"}


def number(state: FizzState) -> dict:
    return {"result": str(state["n"])}
