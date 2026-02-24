from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

llm = ChatGroq(model="openai/gpt-oss-120b")

def get_completion(prompt, temperature=0):
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def chunk_split(text, source_name=None):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=25
    )

    chunks = text_splitter.split_text(text)
