import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(temperature=0):
    """
    Returns the configured Google Gemini model.
    """
    return ChatGoogleGenerativeAI(
        # model="models/gemini-2.5-flash", 
        # model="gemini-pro-latest",
        model="gemini-flash-latest", 
        temperature=temperature,
        api_key=os.getenv("GOOGLE_API_KEY")
    )