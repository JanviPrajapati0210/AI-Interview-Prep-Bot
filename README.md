# 🤖 AI Interview Prep Bot

An AI-powered interview preparation platform built using **Python**, **Streamlit**, **Groq API**, and **ReportLab**. The application helps students and job seekers practice technical interviews, receive AI-generated feedback, analyze performance, identify weak topics, and generate personalized study plans.

---

## 🚀 Features

### 🎯 Practice Mode

* Generate AI-powered interview questions.
* Company-specific interview preparation.
* Role-based question generation.
* Difficulty levels (Easy, Medium, Hard).
* Topic-based questions (DSA, Python, SQL, AI/ML).
* Instant answer evaluation and feedback.
* AI-generated hints for guidance.


### 🎤 Mock Interview Mode

* Simulate a real technical interview.
* Five-question interview sessions.
* Progress tracking throughout the interview.
* AI-based answer evaluation.
* Automatic score calculation.
* Final interview performance report.

### 📊 Analytics Dashboard

* Average score tracking.
* Highest and lowest score analysis.
* Total questions answered.
* Score trend visualization.
* Score distribution analysis.
* Topic-wise performance analytics.
* Strongest and weakest topic identification.
* Interview readiness assessment.

### 📚 AI Study Plan Generator

* Detect weak technical topics automatically.
* Generate personalized study recommendations using AI.
* Focus learning efforts on improvement areas.

### 📄 PDF Report Generation

* Export interview results as PDF reports.
* View performance summaries and recommendations.

---

## 🏢 Supported Companies

* Google
* Amazon
* Microsoft
* Meta
* Netflix
* Apple
* Adobe
* Uber
* TCS
* Infosys

---

## 💼 Supported Roles

* Software Engineer
* AI/ML Engineer
* Data Scientist
* Backend Developer
* Data Analyst

---

## 📚 Supported Topics

* Data Structures & Algorithms (DSA)
* Python
* SQL
* Artificial Intelligence / Machine Learning

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM Integration

* Groq API
* Prompt Engineering

### Reporting

* ReportLab

### Data Processing

* Python Session State
* Analytics & Performance Tracking

---

## 📂 Project Structure

```text
AI-INTERVIEW-PREP-BOT/
│
│
├── pages/
│   ├── 1_Practice_Mode.py
│   ├── 2_Mock_Interview.py
│   ├── 3_Analytics.py
│   └── 4_AI_Study_Plan.py
│
├── utils/
│   ├── __init__.py
│   ├── groq_evaluator.py
│   ├── pdf_generator.py
│   ├── score_tracker.py
│   ├── summary_generator.py
│   └── weak_topic_detector.py
│
├── Home.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone git clone https://github.com/JanviPrajapati0210/AI-Interview-Prep-Bot.git
cd AI-Interview-Prep-Bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the Application

```bash
streamlit run Home.py
```

---

## 🎯 Project Highlights

* AI-powered interview preparation platform.
* LLM-based answer evaluation system.
* Personalized learning recommendations.
* Performance analytics and tracking.
* PDF report generation.
* End-to-end application developed using Python and Streamlit.

---

## 🔮 Future Improvements

* Voice-based interview support.
* Speech-to-text integration.
* User authentication.
* Database integration.
* Interview history storage.
* Additional interview domains and topics.

---

## 👩‍💻 Author

**Janvi Prajapati**

B.Tech in Artificial Intelligence & Machine Learning

Passionate about AI, Machine Learning, Generative AI, and Software Development.

---


