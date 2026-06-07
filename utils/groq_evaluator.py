from groq import Groq
import os
from dotenv import load_dotenv
MODEL_NAME = "llama-3.3-70b-versatile"

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Generate Interview Question


def generate_interview_question(
    company,
    role,
    difficulty,
    topic
):

    prompt = f"""
You are a senior interviewer.

Generate ONE interview question.

Company: {company}
Role: {role}
Difficulty: {difficulty}
Topic: {topic}

Requirements:
- Similar to real interviews
- Based on recent trends
- Return ONLY the question
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# Generate Hint


def generate_hint(question):

    prompt = f"""
    Give a small hint for this interview question.

    Question:
    {question}

    Do not reveal the complete answer.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# Evaluate Answer


def evaluate_answer(question, answer):

    prompt = f"""
You are a senior technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Provide feedback in Markdown format.

Use the following structure:

# Score
Score: X/10

# Strengths
- point

# Weaknesses
- point

# Missing Concepts
- point

# Ideal Answer
Detailed answer

# Interview Recommendation
Recommendation
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_study_plan(weak_topics):

    prompt = f"""
You are an expert technical mentor.

The student performed poorly in:

{weak_topics}

Create a personalized study plan.

Include:

1. Weak Areas
2. Topics to Revise
3. Practice Suggestions
4. Interview Preparation Tips
5. 7-Day Improvement Plan

Format nicely.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content