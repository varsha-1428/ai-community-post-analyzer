import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from models import PostAnalysis

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
print(response) # can also access result.category, result.summary, result.toxic
# try with HumanMessage(content="I hate everyone in this community")