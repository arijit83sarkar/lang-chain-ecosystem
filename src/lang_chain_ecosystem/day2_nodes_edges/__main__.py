# from .simple_graph import runGraph
# from .llm_graph import callLlmGraph
# from .llm_translator_graph import sendNotifications, callTranslator, callMemory

# from .llm_graph_memory import callMemory
# from .linear_graph import callLinearGraph, callConditionalEdges
# from .cycle_edges import callCycleEdges
# from .reducer_graph import callReducer
# from .grade_graph import callGradeGraph
# from .fizzbuzz_graph import callFizzBuzzGraph
# from .exercises.text_normalizer_graph import callTextNormalizerGraph
# from .exercises.temparature_graph import callTemparatureGraph
# from .exercises.rps_graph import callRPSGraph
from .exercises.triangle_graph import callTriangleGraph

if __name__ == "__main__":
    # runGraph()
    # callLlmGraph()
    # sendNotifications()
    # callTranslator()
    # callMemory()
    # callLinearGraph()
    # callConditionalEdges()
    # callCycleEdges()
    # callReducer()
    # callGradeGraph()
    # callFizzBuzzGraph()
    # callTextNormalizerGraph()
    # callTemparatureGraph()
    # callRPSGraph()
    callTriangleGraph()
