from fastapi import FastAPI
from pydantic import BaseModel
from app.chains import get_qa_chain
from app.agent_graph import get_agent_graph
from models.llm import get_llm
from scripts.build_index import build_vector_store

class Query(BaseModel):
    prompt: str

app = FastAPI()

vector_store = build_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
llm = get_llm()
qa_chain = get_qa_chain(llm, retriever)
agent_graph = get_agent_graph(retriever, llm)

@app.post("/ask")
async def ask(query: Query):
    return {"answer": qa_chain.run(query.prompt)}

@app.post("/agent")
async def agent(query: Query):
    result = agent_graph.run({"search_docs": {"query": query.prompt}})
    return {"answer": result["answer"]}