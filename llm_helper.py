from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

llm = ChatGroq(model="openai/gpt-oss-120b")

def get_completion(prompt, temperature=0):
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
