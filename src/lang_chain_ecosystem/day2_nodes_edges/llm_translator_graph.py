from .translator_state import State
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from ..client import loadChatOpenAI
from pathlib import Path
from langgraph.graph import StateGraph, START, END
from langchain_community.tools import GoogleSerperRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv(override=True)

llm = loadChatOpenAI()


# A TOOL
@tool
def send_notification_tool(text: str) -> str:
    """Write you logic to send notifications"""
    return "Notification sent."


search = GoogleSerperRun(api_wrapper=GoogleSerperAPIWrapper())
tools = [search, send_notification_tool]
llm_with_tools = llm.bind_tools(tools)


def sendNotifications() -> None:
    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot_node)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "chatbot")
    builder.add_conditional_edges("chatbot", tools_condition)
    builder.add_edge("tools", "chatbot")

    graph = builder.compile()

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Use your search tool to tell me What is LLM, in one sentence and send me a push notification.",
                }
            ]
        }
    )
    # result = graph.invoke(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": "Use your search tool to give me a list of websites, from India, from where I can find price of Black Pepper "
    #                 "and send me a push notification.",
    #             }
    #         ]
    #     }
    # )
    print(">>>", result["messages"][-1].content)


# A NODE
def chatbot_node(state: State) -> None:
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


def callTranslator() -> None:
    builder = StateGraph(State)

    builder.add_node("chatbot", chatbot_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_node("translator", translator_node)

    builder.add_edge(START, "chatbot")
    builder.add_conditional_edges(
        "chatbot", tools_condition, {"tools": "tools", END: "translator"}
    )
    builder.add_edge("tools", "chatbot")
    builder.add_edge("translator", END)

    graph = builder.compile()

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Use your search tool to tell me What is LLM, in one sentence and send me a push notification.",
                }
            ]
        }
    )
    print(">>>", result["messages"][-1].content)
    print(">>>", result["spanish"])


# A NODE
def translator_node(state: State) -> dict:
    last = state["messages"][-1].content
    prompt = f"Translate this in Spanish, replying with the translation only:\n\n{last}"
    return {"spanish": llm.invoke(prompt).content}
