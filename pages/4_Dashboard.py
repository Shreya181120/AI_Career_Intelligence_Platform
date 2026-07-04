import streamlit as st

st.set_page_config(
    page_title="Career Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Career Dashboard")
st.write("Track your AI Career Journey")

st.markdown("---")

resume_score = st.session_state.get("resume_score", 0)
career_goal = st.session_state.get("career_goal", "Not Selected")
skills = st.session_state.get("skills", [])
missing = st.session_state.get("missing_skills", [])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resume Score", f"{resume_score}%")

with col2:
    st.metric("🎯 Career Goal", career_goal)

with col3:
    st.metric("💻 Skills Found", len(skills))

st.markdown("---")

st.subheader("✅ Current Skills")

if skills:
    for skill in skills:
        st.success(skill)
else:
    st.info("No skills detected yet. Upload your resume.")

st.markdown("---")

st.subheader("📈 Skills To Improve")

if missing:
    for skill in missing[:10]:
        st.warning(skill)
else:
    st.success("Excellent! No missing skills detected.")

st.markdown("---")

st.subheader("🎯 Weekly Goals")

goals = [
    "Complete SQL Practice",
    "Solve 5 Python Problems",
    "Build One Mini Project",
    "Update Resume",
    "Practice Interview Questions"
]

for goal in goals:
    st.checkbox(goal)

st.markdown("---")

st.success("🚀 Keep learning and building projects consistently!")