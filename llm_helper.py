from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

llm = ChatGroq(model="openai/gpt-oss-120b")

def get_completion(prompt: str, temperature:float = 0):
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def chunk_split(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=25)
    return text_splitter.split_documents(documents)
