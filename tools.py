from langchain.tools import tool

memory = None

def set_memory(mem):
    global memory
    memory = mem

vectorstore = None

def set_vectorstore(vs):
    global vectorstore
    vectorstore = vs

@tool
def search_docs(query: str) -> str:
    """Searches the vectorstore for documents similar to the query."""
    docs = vectorstore.similarity_search(query, k=4)
    return "\n\n".join(
    f"Source: {d.metadata.get('source')}\n{d.page_content}"
    for d in docs
)

@tool
def deadline_lookup(_: str = "") -> str:
    """Returns a list of assignment deadlines."""
    deadlines = """
Assignment 1 due: February 25
Assignment 2 due: March 20
Midterm Exam: March 10
Final Project Proposal: April 5
Final Project Demo: April 28
"""
    return deadlines
             
@tool
def add_memory(info: str) -> str:
    """Stores user preferences or information for future chats."""
    memory.add_preference(info)
    return f"Stored in memory: {info}"
             
@tool
def show_history(_: str = ""):
    """Returns the chat history."""
    return memory.get_history()

@tool
def ask_clarification(_: str = "") -> str:
    """Asks for clarification if unsure how to answer a question."""
    return "Ask the user to further clarify their question."
