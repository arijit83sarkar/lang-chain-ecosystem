from .state import State
import random
import subprocess
import sys
from pathlib import Path
from langgraph.graph import StateGraph, START, END

nouns = [
    "Cabbages",
    "Unicorns",
    "Toasters",
    "Penguins",
    "Bananas",
    "Eels",
    "Pickles",
]
adjectives = [
    "outrageous",
    "smelly",
    "pedantic",
    "existential",
    "sparkly",
    "haunted",
]


def silly_node(state: State) -> dict:
    sentence = f"{random.choice(nouns)} are {random.choice(adjectives)}"
    return {"message": [{"role": "assistant", "content": sentence}]}


def save_and_open_graph_image(graph, filename: str = "simple_graph.png") -> None:
    graph_path = Path(__file__).with_name(filename)
    graph_path.write_bytes(graph.get_graph().draw_mermaid_png())
    if sys.platform == "darwin":
        subprocess.run(["open", str(graph_path)])
    elif sys.platform == "win32":
        subprocess.run(["start", "", str(graph_path)], shell=True)
    else:
        subprocess.run(["xdg-open", str(graph_path)])


def runGraph() -> None:
    builder = StateGraph(State)

    builder.add_node("silly", silly_node)
    builder.add_edge(START, "silly")
    builder.add_edge("silly", END)

    graph = builder.compile()

    save_and_open_graph_image(graph)

    result = graph.invoke({"message": [{"role": "user", "content": "say something"}]})
    print(result["message"][-1].content)
