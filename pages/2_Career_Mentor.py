import streamlit as st
from utils.ai_services import generate_career_roadmap

st.set_page_config(
    page_title="Career Mentor",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Career Mentor")
st.write("Generate a personalized career roadmap based on your resume and career goal using IBM watsonx.ai.")

st.markdown("---")

# -----------------------------
# Resume Skills
# -----------------------------

skills = st.session_state.get("skills", [])

if not skills:
    st.warning("⚠ Please upload your resume first from the Resume Analyzer page.")
    st.stop()

# -----------------------------
# Career Selection
# -----------------------------

career = st.selectbox(
    "🎯 Select Your Career Goal",
    [
        "Data Analyst",
        "Data Scientist",
        "Machine Learning Engineer",
        "AI Engineer"
    ]
)

level = st.selectbox(
    "📈 Current Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

study_hours = st.slider(
    "📚 Study Hours Per Day",
    min_value=1,
    max_value=10,
    value=3
)

st.markdown("---")

# -----------------------------
# Current Skills
# -----------------------------

st.subheader("✅ Skills Detected From Resume")

cols = st.columns(3)

for i, skill in enumerate(skills):
    cols[i % 3].success(skill)

st.markdown("---")

# -----------------------------
# Generate AI Roadmap
# -----------------------------

if st.button("🚀 Generate AI Roadmap", use_container_width=True):

    st.session_state["career_goal"] = career

    with st.spinner("Generating personalized roadmap using IBM watsonx.ai..."):

        roadmap = generate_career_roadmap(
            career,
            level,
            study_hours,
            skills
        )

    st.success("✅ AI Roadmap Generated Successfully")

    st.markdown("---")

    st.subheader("🤖 Personalized Career Roadmap")

    st.markdown(roadmap)

    st.markdown("---")

    st.subheader("💡 General Success Tips")

    st.success("✔ Practice coding consistently.")
    st.success("✔ Build real-world projects.")
    st.success("✔ Keep your GitHub updated.")
    st.success("✔ Improve problem-solving skills.")
    st.success("✔ Practice mock interviews every week.")