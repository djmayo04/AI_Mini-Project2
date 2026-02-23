from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

def get_completion(prompt):
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
