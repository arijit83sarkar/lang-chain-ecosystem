from .simple_graph import runGraph
from .llm_graph import callLlmGraph
from .llm_translator_graph import sendNotifications, callTranslator

if __name__ == "__main__":
    # runGraph()
    # callLlmGraph()
    sendNotifications()
    # callTranslator()
