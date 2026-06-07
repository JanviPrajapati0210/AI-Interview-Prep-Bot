import streamlit as st
import re

from utils.groq_evaluator import (
    generate_interview_question,
    evaluate_answer
)

st.title("🎤 Mock Interview Mode")

# Session State

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

# Settings

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

# Start Interview

if st.button("🎤 Start Mock Interview"):

    st.session_state["mi_scores"] = []
    st.session_state["mi_question"] = None
    st.session_state["mi_count"] = 0
    st.session_state["mi_feedback"] = None
    st.session_state["mi_started"] = True

    st.rerun()

# Generate Question


if (
    st.session_state["mi_started"]
    and st.session_state["mi_count"] < 5
    and st.session_state["mi_question"] is None
):

    with st.spinner("Generating Question..."):

        question = generate_interview_question(
            company,
            role,
            difficulty,
            topic
        )

    st.session_state["mi_question"] = question
    st.session_state["mi_count"] += 1

# Interview UI

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

    if st.button("✅ Submit Answer"):

        if answer.strip() == "":

            st.warning(
                "Please enter an answer."
            )

        else:

            with st.spinner(
                "Evaluating..."
            ):

                feedback = evaluate_answer(
                    st.session_state["mi_question"],
                    answer
                )

            st.session_state["mi_feedback"] = feedback

            # Extract Score

            match = re.search(
                r"Score\s*:?\s*(\d+)",
                feedback,
                re.IGNORECASE
            )

            if match:

                score = int(
                    match.group(1))
                if topic not in st.session_state["weak_topics"]:
                    st.session_state["weak_topics"][topic] = []

                st.session_state["weak_topics"][topic].append(score)

                st.session_state["mi_scores"].append(
                    score
                )

                st.session_state["all_scores"].append(
                    {
                      "topic":topic,
                      "score":score
                      }
                )

    # Show Feedback


    if st.session_state["mi_feedback"]:

        st.success(
            "Evaluation Complete"
        )

        st.markdown(
            st.session_state["mi_feedback"]
        )

        if st.session_state["mi_count"] < 5:

            if st.button(
                "➡️ Next Question"
            ):

                st.session_state["mi_question"] = None
                st.session_state["mi_feedback"] = None

                st.rerun()


# Final Report


if len(st.session_state["mi_scores"]) == 5:

    st.divider()

    st.header(
        "🏁 Final Interview Report"
    )

    avg = (
        sum(st.session_state["mi_scores"])
        /
        len(st.session_state["mi_scores"])
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
            "⚠️ Weak Fundamentals"
        )

    st.subheader(
        "📊 Score Breakdown"
    )

    for i, score in enumerate(
        st.session_state["mi_scores"],
        start=1
    ):

        st.write(
            f"Question {i}: {score}/10"
        )