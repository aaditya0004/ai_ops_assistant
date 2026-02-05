import warnings
# Suppress the "GuessedAtParserWarning" from the wikipedia library
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')
import streamlit as st
import time
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from dotenv import load_dotenv


# 1. Load Environment
load_dotenv()

# 2. Page Config
st.set_page_config(page_title="AI Ops Assistant", page_icon="🤖")

st.title("🤖 AI Ops Assistant")
st.markdown("### Powered by Multi-Agent Architecture")
st.info("This assistant plans, executes, and verifies tasks using GitHub and Wikipedia.")

# 3. Sidebar for inputs
with st.sidebar:
    st.header("Control Panel")
    user_input = st.text_area("Enter your task:", height=150, 
                             placeholder="Example: Find the 'langchain' repo on GitHub and explain what it does.")
    run_btn = st.button("🚀 Run Agent Team", type="primary")

# 4. Main Execution Flow
if run_btn and user_input:
    st.divider()
    
    # --- PHASE 1: PLANNING ---
    st.subheader("1️⃣ Planner Agent")
    with st.status("Thinking & Planning...", expanded=True) as status:
        planner = PlannerAgent()
        plan = planner.create_plan(user_input)
        
        if "error" in plan:
            st.error(f"Planning Failed: {plan['error']}")
            st.stop()
            
        st.write("Target Plan:")
        st.json(plan)
        status.update(label="Plan Created!", state="complete", expanded=False)

    # --- PHASE 2: EXECUTION ---
    st.subheader("2️⃣ Executor Agent")
    with st.status("Executing Tools...", expanded=True) as status:
        executor = ExecutorAgent()
        results = executor.execute_plan(plan)
        
        for step, result in results.items():
            st.markdown(f"**{step} Output:**")
            st.code(result) # Display raw tool output in a code block
            
        status.update(label="Execution Complete!", state="complete", expanded=False)

    # --- PHASE 3: VERIFICATION ---
    st.subheader("3️⃣ Verifier Agent")
    with st.spinner("Reviewing final answer..."):
        verifier = VerifierAgent()
        final_response = verifier.verify(user_input, results)
        
    st.success("✅ Task Complete")
    st.markdown("### Final Answer")
    st.markdown(final_response)