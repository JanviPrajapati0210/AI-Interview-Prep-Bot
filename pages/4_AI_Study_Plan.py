import streamlit as st

from utils.groq_evaluator import (
    generate_study_plan
)

st.title("🤖 AI Study Plan")

if "weak_topics" not in st.session_state:

    st.info(
        "Complete a mock interview first."
    )

else:

    weak_topics = []

    for topic, scores in (
        st.session_state["weak_topics"].items()
    ):

        avg = sum(scores) / len(scores)

        if avg < 6:

            weak_topics.append(topic)

    if len(weak_topics) == 0:

        st.success(
            "Excellent! No major weak areas detected."
        )

    else:

        st.write(
            "Detected weak topics:"
        )

        for topic in weak_topics:

            st.write(f"• {topic}")

        if st.button(
            "Generate AI Study Plan"
        ):

            with st.spinner(
                "Creating personalized plan..."
            ):

                plan = generate_study_plan(
                    weak_topics
                )

            st.markdown(plan)