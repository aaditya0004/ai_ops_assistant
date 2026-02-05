# 🤖 AI Ops Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

**An intelligent, multi-agent system that plans, executes, and verifies technical research tasks.**

The **AI Ops Assistant** doesn't just "guess" answers.  
It behaves like a real engineering team — creating a plan, sending a worker to fetch real data from GitHub and the Web, and finally having a manager verify the results before presenting them to you.

---

## 🧠 Architecture: The "Agent Team"

This project uses a **Multi-Agent Architecture** to ensure accuracy and structured reasoning.

| Agent | Role | Description |
|------|------|-------------|
| **1. The Planner** 📝 | *Project Manager* | Analyzes your request and breaks it down into a logical JSON plan. Decides which tools are needed for each step. |
| **2. The Executor** ⚙️ | *The Builder* | Executes the plan by calling real APIs (GitHub, Search) and gathering raw data without judgment. |
| **3. The Verifier** ✅ | *Quality Control* | Reviews raw data against the original question and summarizes findings or reports missing information. |

---

## 🛠️ Integrated APIs & Tools

This system integrates **real third-party APIs** to fetch live data:

1. **GitHub Tool**
   - Uses the GitHub API to find official repositories, star counts, and descriptions  
   - Uses smart sorting (`sort=stars`) to identify the most popular or official repository

2. **Search Tool**
   - Uses **Wikipedia / DuckDuckGo** for definitions, creator information, and general knowledge

3. **LLM Brain**
   - Powered by **Google Gemini Flash** for fast, structured reasoning and decision-making

---

## 🚀 Setup Instructions

Follow these steps to run the assistant locally on `localhost`.

---

### 1. Clone the Repository

```bash
git clone <your-repo-url-here>
cd ai_ops_assistant
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

### 5. Run the Application

```bash
streamlit run main.py
```
The app will automatically open in your browser at http://localhost:8501.

---

## 🧪 Example Prompts to Test
Try these prompts to see the agents in action!

### 🔎 Repository & Creator:

- "Find the 'pytorch' repository on GitHub and explain who created it."

### ⭐ Stars & Definitions:

- "Find the 'flask' repository stars and explain what a microframework is."

### 🔎 Comparison/Research:

- "Search for 'react' on GitHub and tell me who maintains it."


## ⚠️ Known Limitations & Trade-offs
- Search Sensitivity: The Planner is optimized for keyword-based searches (e.g., "PyTorch") rather than natural language questions (e.g., "Who made this?"). This is a design choice to improve Wikipedia hit rates.

- GitHub API Rate Limits: The tool uses unauthenticated GitHub requests, which are limited to 60 per hour. For heavy usage, an API key would be added.

- Linear Execution: Steps are currently executed sequentially. Future improvements would include parallel execution for faster performance.

--- 
Built for the GenAI Intern Assignment.
