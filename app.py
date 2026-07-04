import streamlit as st

st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Intelligence Platform")

st.subheader("Your Personal AI Career Mentor")

st.markdown("---")

st.markdown("## 👋 Welcome")

st.write("""
The AI Career Intelligence Platform helps students prepare for their careers using Artificial Intelligence.

### Features

- 📄 Resume Analysis
- 🎯 Personalized Career Roadmap
- 💻 AI Project Recommendation
- 🎤 AI Interview Coach
- 📊 Career Progress Dashboard

👉 Use the **left sidebar** to explore all modules.
""")

st.markdown("---")

st.info("""
### 🚀 Technology Stack

- Python
- Streamlit
- IBM watsonx.ai
- IBM Granite
- LangChain
""")

st.markdown("---")

st.success("Powered by IBM watsonx.ai + Granite")