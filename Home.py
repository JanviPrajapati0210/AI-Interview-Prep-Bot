import streamlit as st

if st.button("Reset Analytics"):
    st.session_state.clear()
    st.rerun()
    
st.set_page_config(
    page_title="AI Interview Prep Bot",
    layout="wide"
)

st.title("🤖 AI Interview Prep Bot")

st.markdown("""
# Welcome

Practice technical interviews using AI.

### Features

✅ Practice Mode

✅ Mock Interview Mode

✅ AI Generated Questions

✅ AI Evaluation

✅ Performance Analytics

Use the sidebar to select a mode.
""")