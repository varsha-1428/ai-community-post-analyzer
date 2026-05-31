import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from models import PostAnalysis

llm = ChatGroq(model="qwen/qwen3-32b")
structured_llm = llm.with_structured_output(PostAnalysis)

class GraphState(TypedDict):
    post: str
    analysis: PostAnalysis

def analyze_post(state:GraphState):
    result = structured_llm.invoke(state["post"])
    return {
        "analysis": result
    }

builder = StateGraph(GraphState)
builder.add_node("analyze_post", analyze_post)
builder.add_edge(START, "analyze_post")
builder.add_edge("analyze_post", END)
graph = builder.compile()

result = graph.invoke({
    "post": "LangGraph feels difficult for beginners."
})

print(result) # analysis also gets added