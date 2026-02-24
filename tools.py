from langchain.tools import tool

vectorstore = None

def set_vectorstore(vs):
    global vectorstore
    vectorstore = vs

@tool
def search_docs(query: str) -> str:
    """Searches for documents based on the provided query."""
    return "Pretend this searched the syllabus."
