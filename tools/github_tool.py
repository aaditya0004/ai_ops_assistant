import requests
from langchain.tools import tool

@tool
def github_repo_search(query: str):
    """
    Finds the official GitHub repository for a project.
    """
    # 1. CLEAN THE QUERY
    stop_words = ["search for", "find", "the", "repository", "details", "repo", "about", "information"]
    clean_query = query.lower()
    for word in stop_words:
        clean_query = clean_query.replace(word, "")
    clean_query = clean_query.strip()
    
    if not clean_query:
        clean_query = query

    # 2. TARGETED SEARCH (The Fix)
    # We add 'in:name' so it looks for repos NAMED 'pytorch'
    # We still sort by stars to get the official one first
    url = f"https://api.github.com/search/repositories?q={clean_query}+in:name&sort=stars&order=desc"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: GitHub API returned {response.status_code}"
            
        data = response.json()
        
        if "items" in data and len(data['items']) > 0:
            # Get the #1 result
            item = data['items'][0] 
            
            summary = (
                f"Name: {item['full_name']}\n"
                f"Description: {item['description']}\n"
                f"Stars: {item['stargazers_count']}\n"
                f"URL: {item['html_url']}\n"
                f"Language: {item['language']}"
            )
            return summary
        else:
            return f"No repositories found with name '{clean_query}'."
        
    except Exception as e:
        return f"GitHub Tool Error: {str(e)}"