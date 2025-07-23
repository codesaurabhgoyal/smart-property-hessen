from lang_graph.core import Graph
from lang_graph.nodes import LLMNode, RetrieverNode

def get_agent_graph(retriever, llm):
    return Graph(nodes=[
        RetrieverNode(name="search_docs", retriever=retriever),
        LLMNode(name="answer", model=llm)
    ])