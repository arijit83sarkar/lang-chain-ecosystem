from .simple_graph import runGraph
from .llm_graph import callLlmGraph
from .llm_translator_graph import sendNotifications, callTranslator, callMemory

# from .llm_graph_memory import callMemory
from .linear_graph import callLinearGraph, callConditionalEdges

if __name__ == "__main__":
    # runGraph()
    # callLlmGraph()
    # sendNotifications()
    # callTranslator()
    # callMemory()
    callLinearGraph()
    callConditionalEdges()
