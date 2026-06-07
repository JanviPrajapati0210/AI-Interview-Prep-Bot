import streamlit as st

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

st.title("📊 Analytics Dashboard")


# Check Data

if "all_scores" not in st.session_state:
    st.session_state["all_scores"] = []

records = st.session_state["all_scores"]

if len(records) == 0:

    st.info(
        "Complete a mock interview first to see analytics."
    )

else:

    # Support Old and New Formats
    

    if isinstance(records[0], int):

        scores = records

    else:

        scores = [
            item["score"]
            for item in records
        ]

    # Statistics


    avg_score = sum(scores) / len(scores)

    highest_score = max(scores)

    lowest_score = min(scores)

    total_questions = len(scores)

    # Metrics
    

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Score",
            f"{avg_score:.1f}/10"
        )

    with col2:
        st.metric(
            "Highest Score",
            highest_score
        )

    with col3:
        st.metric(
            "Lowest Score",
            lowest_score
        )

    with col4:
        st.metric(
            "Questions Answered",
            total_questions
        )

    st.divider()

    # Score Trend

    st.subheader("📈 Score Trend")

    st.line_chart(scores)

    st.divider()

    # Interview Readiness


    st.subheader("🎯 Interview Readiness")

    if avg_score >= 8:

        st.success(
            "🚀 Ready for Interviews"
        )

    elif avg_score >= 6:

        st.warning(
            "📚 Need More Practice"
        )

    else:

        st.error(
            "⚠️ Focus on Fundamentals"
        )

    st.divider()

    # Score Distribution


    st.subheader("📊 Score Distribution")

    distribution = {
        "0-3": 0,
        "4-6": 0,
        "7-8": 0,
        "9-10": 0
    }

    for score in scores:

        if score <= 3:

            distribution["0-3"] += 1

        elif score <= 6:

            distribution["4-6"] += 1

        elif score <= 8:

            distribution["7-8"] += 1

        else:

            distribution["9-10"] += 1

    st.bar_chart(distribution)

    st.divider()

    # Topic Analytics

    st.subheader("📚 Topic Performance")

    if isinstance(records[0], dict):

        topic_scores = {}

        for item in records:

            topic = item["topic"]
            score = item["score"]

            if topic not in topic_scores:

                topic_scores[topic] = []

            topic_scores[topic].append(score)

        topic_avg = {}

        for topic, values in topic_scores.items():

            topic_avg[topic] = (
                sum(values) / len(values)
            )

        st.bar_chart(topic_avg)

        best_topic = max(
            topic_avg,
            key=topic_avg.get
        )

        weak_topic = min(
            topic_avg,
            key=topic_avg.get
        )

        st.success(
            f"🏆 Strongest Topic: {best_topic}"
        )

        st.warning(
            f"⚠️ Weakest Topic: {weak_topic}"
        )

    else:

        st.info(
            "Topic analytics will appear after completing new interviews."
        )

    st.divider()

    # Performance Summary

    st.subheader("📝 Performance Summary")

    if avg_score >= 8:

        st.write(
            """
            Excellent performance.
            You are performing consistently well
            and appear ready for technical interviews.
            """
        )

    elif avg_score >= 6:

        st.write(
            """
            Good progress.
            Focus on improving weaker concepts
            and practice more interview questions.
            """
        )

    else:

        st.write(
            """
            Your fundamentals need strengthening.
            Spend more time revising core concepts
            and solving interview problems.
            """
        )

    st.divider()

    # Score History
 

    st.subheader("📋 Score History")

    for i, item in enumerate(records, start=1):

        if isinstance(item, dict):

            st.write(
                f"Question {i} | {item['topic']} | {item['score']}/10"
            )

        else:

            st.write(
                f"Question {i} | {item}/10"
            )