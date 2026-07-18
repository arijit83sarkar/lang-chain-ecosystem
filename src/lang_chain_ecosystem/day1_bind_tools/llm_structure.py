from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from ..client import loadChatOpenAI
from .company import Company

load_dotenv(override=True)


def getCompany() -> None:
    llm = loadChatOpenAI()
    llm_with_structure = llm.with_structured_output(Company)

    # messages = [HumanMessage("Tell me about Apple.")]
    comp = llm_with_structure.invoke("Tell me about Apple.")
    print(comp)
    print("Just the ticker: ", comp.ticker)
