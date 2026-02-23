from llm_helper import get_completion
from tools import search_documents

def run_agent(user_input):

    decision_prompt = f"""
Decide ONE:
- call_tool
- answer_directly

User input: {user_input}
"""

    decision = get_completion(decision_prompt)

    if "call_tool" in decision:
        tool_result = search_documents.invoke(user_input)
        return tool_result

    return get_completion(user_input)
