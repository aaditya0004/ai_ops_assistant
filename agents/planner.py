import os
from llm.setup import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm(temperature=0)

    def create_plan(self, user_query):
        system_prompt = """
        You are a Technical Planner Agent.
        
        TOOLS:
        1. 'github_tool': Useful for finding repositories.
        2. 'search_tool': Useful for general knowledge.
        
        RULES:
        - Return ONLY a JSON object with a key 'steps'.
        - 'github_tool' instruction: ONLY THE REPO NAME (e.g. 'pytorch').
        - 'search_tool' instruction: ONLY THE MAIN TOPIC NOUN (e.g. 'PyTorch'). DO NOT include words like 'creator', 'owner', 'who made'.
        
        Reasoning: Wikipedia search fails if query is too specific. Searching 'PyTorch' works; searching 'PyTorch creator' fails.
        
        Example Output:
        {{
            "steps": [
                {{"step_id": 1, "tool": "github_tool", "instruction": "pytorch"}},
                {{"step_id": 2, "tool": "search_tool", "instruction": "PyTorch"}}
            ]
        }}
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{query}")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser
        
        try:
            plan = chain.invoke({"query": user_query})
            return plan
        except Exception as e:
            return {"error": str(e)}