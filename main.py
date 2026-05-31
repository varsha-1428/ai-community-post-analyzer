import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from typing import TypedDict
from models import PostAnalysis

class GraphState(TypedDict):
    post: str
    analysis: PostAnalysis

llm = ChatGroq(model="qwen/qwen3-32b")
structured_llm = llm.with_structured_output(PostAnalysis)

response = structured_llm.invoke([
    SystemMessage(
        content="""
        Analyze the post.

        Return:
        - category
        - summary
        - toxic
        """
    ),
    HumanMessage(content="LangGraph feels very difficult to learn for beginners")
])
print(response)