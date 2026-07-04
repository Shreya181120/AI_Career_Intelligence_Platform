import streamlit as st
from utils.ai_services import generate_project_recommendations

st.set_page_config(
    page_title="Project Advisor",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Project Advisor")
st.write("Get personalized AI-powered project recommendations based on your resume.")

st.markdown("---")

# -----------------------------
# Resume Skills
# -----------------------------

skills = st.session_state.get("skills", [])

if not skills:
    st.warning("⚠ Please upload your resume first from the Resume Analyzer page.")
    st.stop()

# -----------------------------
# Career Details
# -----------------------------

career = st.selectbox(
    "🎯 Select Career Goal",
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

st.markdown("---")

# -----------------------------
# Skills Detected
# -----------------------------

st.subheader("✅ Skills Detected From Resume")

cols = st.columns(3)

for i, skill in enumerate(skills):
    cols[i % 3].success(skill)

st.markdown("---")

# -----------------------------
# AI Recommendation
# -----------------------------

if st.button("🚀 Recommend AI Projects", use_container_width=True):

    with st.spinner("Generating personalized projects using IBM watsonx.ai..."):

        recommendations = generate_project_recommendations(
            career,
            level,
            skills
        )

    st.success("✅ Project Recommendations Generated")

    st.markdown("---")

    st.subheader("🤖 Personalized Project Recommendations")

    st.markdown(recommendations)

    st.markdown("---")

    st.subheader("💡 Tips")

    st.success("✔ Upload every project to GitHub.")
    st.success("✔ Deploy projects using Streamlit.")
    st.success("✔ Write a professional README.")
    st.success("✔ Add projects to LinkedIn and Resume.")