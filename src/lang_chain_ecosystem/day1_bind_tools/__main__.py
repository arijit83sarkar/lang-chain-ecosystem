from .llm_tool import run
from .llm_structure import run as run_structure
from langchain_core.tools import tool


@tool
def tool_add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


def addNumbers() -> None:
    print("args :: ", tool_add_numbers.args)
    print("Sum :: ", tool_add_numbers.invoke({"a": 10, "b": 20}))


@tool
def tool_get_weather(city: str) -> str:
    """Returns the weather of a city."""
    fake_weather = {
        "KOL": "40 degree Celcious",
        "MUM": "38.9 degree Celcious",
        "DEL": "45 degree Celcious",
        "CHEN": "43 degree Celcious",
    }

    print("input: ", city)
    return fake_weather.get(city, "Data is not available.")


def getWeather() -> None:
    print("name: ", tool_get_weather.name)
    print("description: ", tool_get_weather.description)
    print("args: ", tool_get_weather.args)
    print("weather: ", tool_get_weather.invoke({"city": "KOL"}))


if __name__ == "__main__":
    # run_structure()
    # run()
    addNumbers()
    getWeather()
