import os
from llm.setup import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class VerifierAgent:
    def __init__(self):
        self.llm = get_llm(temperature=0.7)

    def verify(self, original_query, tool_outputs):
        """
        Synthesizes the tool outputs into a final answer.
        """
        
        system_prompt = """
        You are a Quality Control Verifier.
        You have the User's Original Request and the Results from the technical team.
        
        Your job:
        1. Check if the results answer the request.
        2. Combine the raw data into a clear, professional answer.
        3. If something is missing, explicitly mention what is missing.
        
        Format the final answer nicely with headers or bullet points if needed.
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "Original Request: {query}\n\nTool Results: {results}")
        ])
        
        chain = prompt | self.llm | StrOutputParser()
        
        try:
            # We convert the dictionary of results to a string so the LLM can read it
            results_str = str(tool_outputs)
            final_answer = chain.invoke({"query": original_query, "results": results_str})
            return final_answer
        except Exception as e:
            return f"Error during verification: {str(e)}"


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    agent = VerifierAgent()
    
    # Fake inputs (simulating the previous steps)
    fake_query = "What is Flask and how many stars does it have?"
    fake_results = {
        "Step 1": "Repo: pallets/flask, Stars: 71,000",
        "Step 2": "Flask is a micro web framework written in Python."
    }
    
    print("✅ Verifying and Summarizing...")
    response = agent.verify(fake_query, fake_results)
    print("\nFINAL ANSWER:\n" + response)