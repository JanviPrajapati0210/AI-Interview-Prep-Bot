import streamlit as st

from utils.groq_evaluator import (
    generate_interview_question,
    generate_hint,
    evaluate_answer
)

st.title("🎯 Practice Mode")

company = st.selectbox(
    "Company",
    [
        "Google",
        "Amazon",
        "Microsoft",
        "Meta",
        "Netflix",
        "Apple",
        "Adobe",
        "Uber",
        "TCS",
        "Infosys"
    ]
)

role = st.selectbox(
    "Role",
    [
        "Software Engineer",
        "AI/ML Engineer",
        "Data Scientist",
        "Backend Developer",
        "Data Analyst"
    ]
)

difficulty = st.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)
topic = st.selectbox(
    "📚 Topic",
    [
        "DSA",
        "Python",
        "SQL",
        "AI/ML"
    ]
)

if "practice_question" not in st.session_state:
    st.session_state["practice_question"] = None

if st.button("Generate Question"):

    question = generate_interview_question(
        company,
        role,
        difficulty,
        topic
    )

    st.session_state["practice_question"] = question

if st.session_state["practice_question"]:

    st.subheader("Question")

    st.write(
        st.session_state["practice_question"]
    )

    if st.button("Show Hint"):

        hint = generate_hint(
            st.session_state[
                "practice_question"
            ]
        )

        st.info(hint)

    answer = st.text_area(
        "Your Answer"
    )

    if st.button("Evaluate"):

        feedback = evaluate_answer(
            st.session_state[
                "practice_question"
            ],
            answer
        )

        st.markdown(feedback)