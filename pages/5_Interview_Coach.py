import streamlit as st
import random

from utils.ai_services import generate_interview_feedback

st.set_page_config(
    page_title="Interview Coach",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Coach")

st.write("Practice technical interview questions and get AI-powered feedback.")

st.markdown("---")

career = st.selectbox(
    "🎯 Select Career",
    [
        "Data Analyst",
        "Data Scientist",
        "Machine Learning Engineer",
        "AI Engineer"
    ]
)

difficulty = st.selectbox(
    "📈 Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

questions = {

    "Data Analyst":[
        "What is SQL?",
        "Difference between INNER JOIN and LEFT JOIN?",
        "Explain Data Cleaning.",
        "What is Power BI?",
        "Difference between Mean and Median?"
    ],

    "Data Scientist":[
        "What is Machine Learning?",
        "Difference between Supervised and Unsupervised Learning?",
        "Explain Overfitting.",
        "What is Cross Validation?",
        "Explain Random Forest."
    ],

    "Machine Learning Engineer":[
        "Explain Gradient Descent.",
        "What is CNN?",
        "Difference between TensorFlow and PyTorch?",
        "How do you deploy ML models?",
        "Explain Bias vs Variance."
    ],

    "AI Engineer":[
        "What are LLMs?",
        "Explain RAG.",
        "What is Prompt Engineering?",
        "Explain Agentic AI.",
        "What is LangChain?"
    ]
}

# -----------------------------
# Save Question
# -----------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if st.button("🎯 Generate Interview Question", use_container_width=True):

    st.session_state.current_question = random.choice(
        questions[career]
    )

# -----------------------------
# Show Question
# -----------------------------

if st.session_state.current_question:

    st.subheader("📝 Interview Question")

    st.info(st.session_state.current_question)

    answer = st.text_area(
        "Write Your Answer",
        height=200
    )

    if st.button("🤖 Evaluate My Answer", use_container_width=True):

        if answer.strip() == "":
            st.warning("Please write your answer first.")

        else:

            with st.spinner("IBM watsonx.ai is evaluating your answer..."):

                feedback = generate_interview_feedback(
                    st.session_state.current_question,
                    answer
                )

            st.markdown("---")

            st.subheader("🤖 AI Interview Feedback")

            st.markdown(feedback)

            st.markdown("---")

            st.success("Keep practicing regularly to improve your interview performance! 🚀")