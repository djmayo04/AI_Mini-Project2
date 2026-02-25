from llm_helper import get_completion
from tools import search_docs
from memory import Memory

memory = Memory()

def run_agent(user_input: str):
    memory.add_user(user_input)

    decision_prompt = f"""
You are an academic assistant for a university-level Artificial Intelligence course.

Your responsibilities:
- Help students understand AI concepts.
- Provide ACCURATE information about course materials such as assignments, rubric, syllabus, deadlines, and FAQs.
- Use available tools when necessary to retrieve official course information. 

Available tools: 
-search_docs: Searches official course documents (assignments, rubric, syllabus, FAQ).

Rules:
1. If the question asks about course policies, deadlines, grading, assignment instructions, or syllabus content → call the appropriate tool.
2. If the question asks about general AI concepts (e.g., PEAS, intelligent agents, search algorithms) → answer directly.
3. If unsure whether the answer exists in course documents → call the tool.
4. Do NOT guess or fabricate course information.

User question:
{user_input}

Respond in the following format ONLY:

Action: <call_tool or answer_directly>
Tool: <tool_name or none>
"""

    decision = get_completion(decision_prompt)

    if "call_tool" in decision:
        
        tool_result = search_docs.invoke(user_input)
        
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


    decision = get_completion(decision_prompt)

    if "call_tool" in decision:
        
        tool_result = search_docs.invoke(user_input)
        
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
