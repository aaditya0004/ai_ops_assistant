from langchain.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

@tool
def web_search(query: str):
    """
    Searches for general knowledge, creators, and definitions using Wikipedia.
    """
    try:
        # We use Wikipedia because it is stable and reliable for assignments
        wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
        
        result = wiki.run(query)
        
        if not result or "No good Wikipedia Search Result" in result:
            return "No information found."
            
        return result
        
    except Exception as e:
        return f"Search Error: {str(e)}"