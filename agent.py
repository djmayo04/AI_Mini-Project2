from llm_helper import get_completion
from tools import search_docs, deadline_lookup, add_memory, show_history, ask_clarification, set_memory
from memory import Memory

memory = Memory()
set_memory(memory)

def format_preferences(memory) -> str:
    prefs = memory.get_preferences()
    if not prefs:
        return "(none)"
    return "\n".join(f"- {p}" for p in prefs)
    
def run_agent(user_input: str):
    memory.add_user(user_input)

    prefs_text = format_preferences(memory)
    
    decision_prompt = f"""
You are an academic assistant for a university-level Artificial Intelligence course.

Stored user preferences/facts (use these when relevant): {prefs_text}

Your responsibilities:
- Help students understand AI concepts.
- Provide ACCURATE information about course materials such as assignments, rubric, syllabus, deadlines, and FAQs.
- Use available tools when necessary to retrieve official course information. 

Available tools: 
- search_docs: Searches official course documents (assignments, rubric, syllabus, FAQ).
- deadline_lookup: Return the official list of course deadlines.
- show_history: Show the current chat history.
- add_memory: Store a user preference/fact for later (e.g., "My name is Ana and I can study 2 hours per day.").
- ask_clarification: Ask the user a clarifying question when the request is ambiguous.

Tool selection rules:
1) If the user asks for a due date / deadline use  deadline_lookup.
2) If the user asks to "show history" / "what did I say earlier" use show_history.
3) If the user asks you to remember a preference/fact use add_memory.
4) If the question is about course policies, grading, rubric, assignment instructions, syllabus/FAQ content use search_docs.
5) If the question is unclear/underspecified use ask_clarification.
6) If the question is general AI concept help (PEAS, intelligent agents, search, ML basics) then answer_directly.

User question: ###
{user_input}
###
Respond in the following format ONLY:

Action: <call_tool or answer_directly>
Tool: <tool_name or none>
""".strip()

    decision = get_completion(decision_prompt).lower()

    if "call_tool" in decision:

        if "deadline_lookup" in decision:
            tool_result = deadline_lookup.invoke("")

        elif "show_history" in decision:
            tool_result = show_history.invoke("")

        elif "add_memory" in decision:
            tool_result = add_memory.invoke(user_input)

        elif "ask_clarification" in decision:
            tool_result = ask_clarification.invoke("")

        else:  # default to search_docs
            tool_result = search_docs.invoke(user_input)
            
        final_prompt = f"""
You are an academic assistant for an AI course.

Stored user preferences/facts (use these when relevant):
{prefs_text}

Use ONLY the tool output below to answer the user's question. 
If the answer is not in the tool output, say you couldn't find it and suggest what to ask/look up.

Tool output:
{tool_result}

User question:
{user_input}
""".strip()
        response = get_completion(final_prompt)

    else:
        direct_prompt = f"""
You are an academic assistant for a university-level Artificial Intelligence course.

Stored user preferences/facts (use these when relevant):
{prefs_text}

User question:
{user_input}
""".(strip)
        response = get_completion(direct_prompt)
    
    memory.add_assistant(response)

    return response
