import streamlit as st
import re

from utils.groq_evaluator import (
    generate_interview_question,
    evaluate_answer
)

st.set_page_config(
    page_title="Mock Interview",
    layout="wide"
)

st.title("🎤 Mock Interview Mode")

# -------------------------
# Session State
# -------------------------

if "mi_scores" not in st.session_state:
    st.session_state["mi_scores"] = []

if "mi_question" not in st.session_state:
    st.session_state["mi_question"] = None

if "mi_count" not in st.session_state:
    st.session_state["mi_count"] = 0

if "mi_feedback" not in st.session_state:
    st.session_state["mi_feedback"] = None

if "mi_started" not in st.session_state:
    st.session_state["mi_started"] = False

if "all_scores" not in st.session_state:
    st.session_state["all_scores"] = []

if "weak_topics" not in st.session_state:
    st.session_state["weak_topics"] = {}

if "asked_questions" not in st.session_state:
    st.session_state["asked_questions"] = []

if "answer_submitted" not in st.session_state:
    st.session_state["answer_submitted"] = False

# -------------------------
# Settings
# -------------------------

company = st.selectbox(
    "🏢 Company",
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
    "💼 Role",
    [
        "Software Engineer",
        "AI/ML Engineer",
        "Data Scientist",
        "Backend Developer",
        "Data Analyst"
    ]
)

difficulty = st.selectbox(
    "📊 Difficulty",
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

# -------------------------
# Start Interview
# -------------------------

if st.button("🎤 Start Mock Interview"):

    st.session_state["mi_scores"] = []
    st.session_state["mi_question"] = None
    st.session_state["mi_count"] = 0
    st.session_state["mi_feedback"] = None
    st.session_state["asked_questions"] = []
    st.session_state["answer_submitted"] = False

    st.session_state["mi_started"] = True

    st.rerun()

# -------------------------
# Generate Question
# -------------------------

if (
    st.session_state["mi_started"]
    and st.session_state["mi_count"] < 5
    and st.session_state["mi_question"] is None
):

    with st.spinner("Generating Interview Question..."):

        question = generate_interview_question(
            company,
            role,
            difficulty,
            topic,
            st.session_state["asked_questions"]
        )

    st.session_state["mi_question"] = question

    st.session_state["asked_questions"].append(
        question
    )

    st.session_state["mi_count"] += 1

# -------------------------
# Interview UI
# -------------------------

if st.session_state["mi_question"]:

    st.progress(
        st.session_state["mi_count"] / 5
    )

    st.subheader(
        f"Question {st.session_state['mi_count']} of 5"
    )

    st.write(
        st.session_state["mi_question"]
    )

    answer = st.text_area(
        "Your Answer",
        height=200
    )

    if (
        st.button("✅ Submit Answer")
        and not st.session_state["answer_submitted"]
    ):

        if answer.strip() == "":

            st.warning(
                "Please enter your answer."
            )

        else:

            with st.spinner(
                "AI Interviewer Evaluating..."
            ):

                feedback = evaluate_answer(
                    st.session_state["mi_question"],
                    answer
                )

            st.session_state["mi_feedback"] = feedback

            match = re.search(
                r"Score\s*:?\s*(\d+)",
                feedback,
                re.IGNORECASE
            )

            if match:

                score = int(
                    match.group(1)
                )

                # Weak Topic Tracking

                if topic not in st.session_state["weak_topics"]:

                    st.session_state[
                        "weak_topics"
                    ][topic] = []

                st.session_state[
                    "weak_topics"
                ][topic].append(score)

                # Mock Scores

                st.session_state[
                    "mi_scores"
                ].append(score)

                # Analytics Storage

                st.session_state[
                    "all_scores"
                ].append(
                    {
                        "topic": topic,
                        "company": company,
                        "difficulty": difficulty,
                        "question":
                        st.session_state[
                            "mi_question"
                        ],
                        "score": score
                    }
                )

            st.session_state[
                "answer_submitted"
            ] = True

    # -------------------------
    # Feedback
    # -------------------------

    if st.session_state["mi_feedback"]:

        st.success(
            "Evaluation Complete"
        )

        st.markdown(
            st.session_state["mi_feedback"]
        )

        if (
            st.session_state["mi_count"]
            < 5
        ):

            if st.button(
                "➡️ Next Question"
            ):

                st.session_state[
                    "mi_question"
                ] = None

                st.session_state[
                    "mi_feedback"
                ] = None

                st.session_state[
                    "answer_submitted"
                ] = False

                st.rerun()

# -------------------------
# Final Report
# -------------------------

if len(st.session_state["mi_scores"]) == 5:

    st.divider()

    st.header(
        "🏁 Final Interview Report"
    )

    avg = (
        sum(
            st.session_state["mi_scores"]
        )
        /
        len(
            st.session_state["mi_scores"]
        )
    )

    st.metric(
        "Final Score",
        f"{avg:.1f}/10"
    )

    if avg >= 8:

        st.success(
            "🚀 Strong Candidate"
        )

    elif avg >= 6:

        st.warning(
            "📚 Needs Improvement"
        )

    else:

        st.error(
            "⚠️ Focus on Fundamentals"
        )

    st.subheader(
        "📊 Question-wise Scores"
    )

    for i, score in enumerate(
        st.session_state["mi_scores"],
        start=1
    ):

        st.write(
            f"Question {i}: {score}/10"
        )