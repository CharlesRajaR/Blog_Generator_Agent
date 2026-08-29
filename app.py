import uvicorn
from dotenv import load_dotenv
from src.blog_generator_agent.graphs.graph_builder import GraphBuilder
from fastapi import FastAPI, Request
from src.blog_generator_agent.llms.gemini_llm import GeminiLLM
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

class Topic(BaseModel):
    topic:str

@app.post("/blogs")
async def create_blogs(request: Topic):


    topic = request.topic
    print(topic)


    gemini_llm = GeminiLLM()
    llm=gemini_llm.get_llm()

    graph_builder = GraphBuilder(llm)
    if topic:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic":topic})

    return {"data":state}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port = 8000)