from .translator_state import TranslatorState
from .state import State
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from ..client import loadChatOpenAI
from langgraph.graph import StateGraph, START, END
from langchain_community.tools import GoogleSerperRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

load_dotenv(override=True)

llm = loadChatOpenAI()


@tool
def send_notification_tool() -> str:
    """Write you logic to send notifications"""
    return "Notification sent."


search = GoogleSerperRun(api_wrapper=GoogleSerperAPIWrapper())
tools = [search, send_notification_tool]
llm_with_tools = llm.bind_tools(tools)


# A NODE
def chatbot_node(state: State) -> None:
    """returns a chat message"""
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# A NODE
@tool
def translator_node(state: TranslatorState) -> dict:
    """translates a message in spanish"""
    last_message = state["messages"][-1].content
    prompt = (
        f"Translate this in Spanish, replying with the translation only\n{last_message}"
    )
    return {"spanish": llm.invoke(prompt).content}


def callMemory() -> None:
    memory = MemorySaver()
    builder = StateGraph(TranslatorState)

    builder.add_node("chatbot", chatbot_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_node("translator", translator_node)

    builder.add_edge(START, "chatbot")
    builder.add_conditional_edges(
        "chatbot", tools_condition, {"tools": "tools", END: "translator"}
    )
    builder.add_edge("translator", END)
    builder.add_edge("tools", "chatbot")

    graph = builder.compile(checkpointer=memory)

    config = {"configurable": {"thread_id": "conversation-1"}}
    graph.invoke(
        {"messages": [{"role": "user", "content": "Hi, my name is Ed."}]}, config
    )
    second = graph.invoke(
        {"messages": [{"role": "user", "content": "What is my name?"}]}, config
    )
    print(">>>", second["messages"][-1].content)
    print(">>>", second["spanish"])
