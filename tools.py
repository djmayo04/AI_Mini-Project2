from langchain.tools import tool

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
def deadline_lookup
    deadlines = []
    return 

             
@tool
def add_memory


             
@tool
def show_history(history: str) -> str:
    return agent.memory.get_history()

@tool
def ask_clarification
    return "ask for clarification message"
