import streamlit as st

from utils.resume_parser import extract_text_from_pdf
from utils.resume_analyzer import analyze_resume
from utils.ai_services import generate_resume_feedback

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer")
st.write("Upload your resume and let AI analyze it using IBM watsonx.ai.")

# -------------------------
# Upload Resume
# -------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("👆 Please upload your resume to get AI analysis.")
    st.stop()

# -------------------------
# Resume Uploaded
# -------------------------

st.success("✅ Resume uploaded successfully!")
st.write("**Filename:**", uploaded_file.name)

# -------------------------
# Extract Resume Text
# -------------------------

resume_text = extract_text_from_pdf(uploaded_file)

# -------------------------
# Analyze Resume
# -------------------------

score, skills, education, experience = analyze_resume(resume_text)

# -------------------------
# Save Data for Other Pages
# -------------------------

st.session_state["resume_score"] = score
st.session_state["skills"] = skills
st.session_state["education"] = education
st.session_state["experience"] = experience

# -------------------------
# Resume Preview
# -------------------------

st.subheader("📄 Resume Preview")

st.text_area(
    "Extracted Resume Text",
    resume_text,
    height=250
)

st.markdown("---")

# -------------------------
# Resume Analysis
# -------------------------

st.subheader("📊 Resume Analysis")

col1, col2 = st.columns(2)

with col1:

    st.metric("Resume Score", f"{score}%")

    st.success("### ✅ Skills Detected")

    if skills:
        for skill in skills:
            st.write(f"✔ {skill}")
    else:
        st.warning("No technical skills detected.")

with col2:

    st.subheader("🎓 Education")
    st.info(education)

    st.subheader("💼 Experience")
    st.info(experience)

st.markdown("---")

# -------------------------
# IBM AI Resume Feedback
# -------------------------

st.subheader("🤖 AI Resume Feedback")

with st.spinner("Analyzing your resume using IBM watsonx.ai..."):

    feedback = generate_resume_feedback(
        score,
        skills,
        education,
        experience
    )

st.markdown(feedback)

st.markdown("---")

st.success("✅ Resume analysis completed successfully!")