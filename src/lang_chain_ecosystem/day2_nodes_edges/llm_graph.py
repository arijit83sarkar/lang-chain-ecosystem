import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from ..client import loadChatOpenAI
from .state import State
import subprocess
import sys
from pathlib import Path
from langgraph.graph import StateGraph, START, END

load_dotenv(override=True)


def callLlmGraph() -> None:
    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot_node)
    builder.add_edge(START, "chatbot")
    builder.add_edge("chatbot", END)
    graph = builder.compile()

    # save_and_open_graph_image(graph)

    result = graph.invoke(
        {"message": [{"role": "user", "content": "What is LLM, in one sentence?"}]}
    )
    print(">>>", result["message"][-1].content)


def chatbot_node(state: State) -> None:
    llm = loadChatOpenAI()
    return {"message": [llm.invoke(state["message"])]}


def save_and_open_graph_image(graph, filename: str = "simple_graph.png") -> None:
    graph_path = Path(__file__).with_name(filename)
    graph_path.write_bytes(graph.get_graph().draw_mermaid_png())
    if sys.platform == "darwin":
        subprocess.run(["open", str(graph_path)])
    elif sys.platform == "win32":
        subprocess.run(["start", "", str(graph_path)], shell=True)
    else:
        subprocess.run(["xdg-open", str(graph_path)])
