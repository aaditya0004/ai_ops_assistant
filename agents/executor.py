from tools.github_tool import github_repo_search
from tools.search_tool import web_search  

class ExecutorAgent:
    def __init__(self):
        self.search = web_search
        self.github = github_repo_search

    def execute_plan(self, plan):
        print("⚙️ Executing Plan...")
        results = {}
        steps = plan.get('steps', [])
        
        for step in steps:
            tool_name = step.get('tool')
            instruction = step.get('instruction')
            step_id = step.get('step_id')
            
            print(f"  → Step {step_id}: Calling {tool_name} with input: '{instruction}'")
            
            try:
                output = ""
                if tool_name == 'github_tool':
                    output = self.github.invoke(instruction)
                
                elif tool_name == 'search_tool' or tool_name == 'wiki_tool':
                    # map both names to our new Search Engine
                    output = self.search.invoke(instruction)
                
                else:
                    output = f"Error: Unknown tool '{tool_name}'"
                
                results[f"Step {step_id}"] = output
                print(f"    ✅ Success.")
                
            except Exception as e:
                results[f"Step {step_id}"] = f"Error: {str(e)}"
                print(f"    ❌ Error: {str(e)}")
                
        return results