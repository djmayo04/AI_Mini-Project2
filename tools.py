from langchain.tools import tool

@tool
def search_docs(query: str) -> str:
    """Searches for documents based on the provided query."""
    return "Pretend this searched the syllabus."
