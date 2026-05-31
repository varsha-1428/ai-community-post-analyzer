import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
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

state = {
    "post": "LangGraph feels difficult for beginners."
}

result = analyze_post(state)

print(result)