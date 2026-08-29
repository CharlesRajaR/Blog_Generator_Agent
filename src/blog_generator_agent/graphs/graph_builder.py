from langgraph.graph import START, StateGraph, END
from src.blog_generator_agent.llms.gemini_llm import GeminiLLM
from src.blog_generator_agent.state.blog_state import  BlogState
from src.blog_generator_agent.nodes.blog_node import BlogNode


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_graph(self):
        self.blog_nodes = BlogNode(self.llm)

        self.graph.add_node("title_creation", self.blog_nodes.title_creation)
        self.graph.add_node("content_generation", self.blog_nodes.content_generation)

        self.add_edge(START, "title_creation")
        self.add_edge("title_creation", "content_generation")
        self.add_edge("content_generation", END)

        return self.graph

    def setup_graph(self, usecase:str):
        if usecase == "topic":
            self.build_graph()

        return self.graph.compile()