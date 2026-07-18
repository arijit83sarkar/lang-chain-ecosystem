import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from .client import loadChatOpenAI

load_dotenv(override=True)


def callLLM() -> None:
    llm = loadChatOpenAI()

    """ for simple query """
    # response = llm.invoke("what does it mean for an AI agent to be autonomous.")
    # print(response.content)

    """ for Stream """
    # for chunk in llm.stream("tell me a two line poem about autonomous agent"):
    #     print(chunk.content, end="", flush=True)

    """ Messages """
    messages = [
        SystemMessage("You are a terse assistant who answers in exactly five words."),
        HumanMessage("what is the capital of India?"),
    ]
    # print(llm.invoke(messages).content)

    print("name: ", get_share_prices.name)
    print("description: ", get_share_prices.description)
    print("args: ", get_share_prices.args)
    print("share price: ", get_share_prices.invoke({"symbol": "GOOG"}))


@tool
def get_share_prices(symbol: str) -> float:
    """Returns the current share price for a given ticker symbol."""
    fake_prices = {"APPL": 340.9, "GOOG": 398.7, "AMZN": 378.6}
    return fake_prices.get(symbol.upper, 0.0)


if __name__ == "__main__":
    callLLM()
