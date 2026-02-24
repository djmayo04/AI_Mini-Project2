from langchain.tools import tool

vectorstore = None

def set_vectorstore(vs):
    global vectorstore
    vectorstore = vs

@tool
def search_docs(query: str) -> str:
    """Searches the vectorstore for documents similar to the query."""
    docs = vectorstore.similary_search(query, k=4)
    return "something"
