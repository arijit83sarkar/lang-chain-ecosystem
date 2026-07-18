from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

from ..client import loadChatOpenAI

load_dotenv(override=True)


@tool
def tool_get_share_prices(symbol: str) -> float:
    """Returns the current share price for a given ticker symbol."""
    fake_prices = {"APPL": 340.9, "GOOG": 398.7, "AMZN": 378.6}
    return fake_prices.get(symbol.upper(), 0.0)


def fetchSharePrice() -> None:
    llm = loadChatOpenAI()
    llm_with_tools = llm.bind_tools([tool_get_share_prices])

    messages = [HumanMessage("what is the share price of GOOG?")]
    ai_message = llm_with_tools.invoke(messages)
    messages.append(ai_message)

    print("tool_calls: ", ai_message.tool_calls)

    for tool_call in ai_message.tool_calls:
        result = tool_get_share_prices.invoke(tool_call["args"])
        messages.append(ToolMessage(content=str(result), tool_call_id=tool_call["id"]))

    final_response = llm_with_tools.invoke(messages)
    print("final response: ", final_response.content)


@tool
def tool_get_weather(city: str) -> str:
    """returns the weather of a city"""
    fake_weather = {
        "Kolkata": "40 degree Celcious",
        "Mumbai": "38.9 degree Celcious",
        "Delhi": "45 degree Celcious",
        "Chenai": "43 degree Celcious",
    }
    return fake_weather.get(city, "Data is not available.")


def fetchWeather() -> None:
    llm = loadChatOpenAI()
    llm_with_tool = llm.bind_tools([tool_get_weather])

    message = [HumanMessage("what is the weather of Kolkata?")]
    ai_message = llm_with_tool.invoke(message)
    message.append(ai_message)

    print("tool_calls: ", ai_message.tool_calls)

    for tool_calls in ai_message.tool_calls:
        result = tool_get_weather.invoke(tool_calls["args"])
        message.append(ToolMessage(content=str(result), tool_call_id=tool_calls["id"]))

    final_response = llm_with_tool.invoke(message)
    print("final response :: ", final_response.content)
