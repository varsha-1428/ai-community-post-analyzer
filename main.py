import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="qwen/qwen3-32b")
response = llm.invoke("Hi, How are you?")
print(response.content)