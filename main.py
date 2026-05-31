import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
llm = ChatGroq(model="qwen/qwen3-32b")
response = llm.invoke([
    SystemMessage(content="Reply in exactly 3 words"),
    HumanMessage(content="I am learning langgraph.")
])
print(response.content)