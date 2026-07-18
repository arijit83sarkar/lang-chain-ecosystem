from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

from ..client import loadChatOpenAI

load_dotenv(override=True)


@tool
def get_share_prices(symbol: str) -> float:
    """Returns the current share price for a given ticker symbol."""
    fake_prices = {"APPL": 340.9, "GOOG": 398.7, "AMZN": 378.6}
    return fake_prices.get(symbol.upper(), 0.0)


def run() -> None:
    llm = loadChatOpenAI()
    llm_with_tools = llm.bind_tools([get_share_prices])

    messages = [HumanMessage("what is the share price of GOOG?")]
    ai_message = llm_with_tools.invoke(messages)
    messages.append(ai_message)

    print("tool_calls: ", ai_message.tool_calls)

    for tool_call in ai_message.tool_calls:
        result = get_share_prices.invoke(tool_call["args"])
        messages.append(
            ToolMessage(content=str(result), tool_call_id=tool_call["id"])
        )

    final_response = llm_with_tools.invoke(messages)
    print("final response: ", final_response.content)