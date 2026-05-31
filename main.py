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
    action: str

def analyze_post(state:GraphState):
    result = structured_llm.invoke(state["post"])
    return {
        "analysis": result
    }

builder = StateGraph(GraphState)
builder.add_node("analyze_post", analyze_post)
builder.add_edge(START, "analyze_post")
# builder.add_edge("analyze_post", END)

def moderation_decision(state:GraphState):
    if state["analysis"].toxic:
        return "review"
    return "publish"

def publish_post(state:GraphState):
    return {
        "action": "publish"
    }

def moderator_review(state: GraphState):
    return {
        "action": "review"
    }

builder.add_node("publish", publish_post)
builder.add_node("review", moderator_review)
builder.add_conditional_edges(
    "analyze_post",
    moderation_decision,
    {
        "publish": "publish",
        "review": "review"
    }
)
builder.add_edge("publish",END)
builder.add_edge("review",END)
graph = builder.compile()

result = graph.invoke({
    "post": "LangGraph feels difficult for beginners."
})

print(result) # analysis, action also gets added