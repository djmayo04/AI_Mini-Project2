from llm_helper import get_completion
from tools import search_documents
from memory import Memory

memory = Memory()

def run_agent(user_input: str):
    memory.add_user(user_input)

    decision_prompt = f"""
You are a rational academic assistant.

Decide ONE action:
- call_tool
- answer_directly

User input: {user_input}
Respond with only the action name.
"""

    decision = get_completion(decision_prompt)

    if "call_tool" in decision:
        
        tool_result = search_documents.invoke(user_input)
        
        final_prompt = f"""
Use the following tool result to answer the user:

{tool_result}

User question:
{user_input}
"""
        response = get_completion(final_prompt)

    else:
        response = get_completion(user_input)
    
    memory.add_assistant(response)

    return response
