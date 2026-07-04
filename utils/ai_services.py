from utils.granite_api import generate_response

# ==========================================================
# Resume Feedback
# ==========================================================

def generate_resume_feedback(score, skills, education, experience):

    prompt = f"""
You are a professional ATS Resume Reviewer.

Analyze the following resume.

Resume Score:
{score}/100

Education:
{education}

Experience:
{experience}

Technical Skills:
{skills}

Provide:

1. Overall Resume Review
2. Resume Strengths
3. Resume Weaknesses
4. ATS Improvement Suggestions
5. Recommended Certifications
6. Final Resume Rating out of 10

Keep the response under 250 words.
"""

    return generate_response(prompt)


# ==========================================================
# Career Roadmap + Skill Gap Analysis
# ==========================================================

def generate_career_roadmap(career, level, study_hours, skills):

    prompt = f"""
You are an AI Career Mentor.

Candidate Career Goal:
{career}

Current Skill Level:
{level}

Study Hours Per Day:
{study_hours}

Current Skills:
{skills}

Generate a personalized roadmap.

Include:

1. Required Skills for this career
2. Current Skills
3. Missing Skills
4. 30-Day Learning Roadmap
5. Recommended Certifications
6. Recommended Projects
7. Interview Preparation Tips

Keep the response under 350 words.
"""

    return generate_response(prompt)


# ==========================================================
# Project Recommendation
# ==========================================================

def generate_project_recommendations(career, level, skills):

    prompt = f"""
You are an AI Project Mentor.

Candidate Career Goal:
{career}

Current Skill Level:
{level}

Current Technical Skills:
{skills}

Recommend 5 portfolio projects suitable for this candidate.

For each project provide:

1. Project Name
2. Difficulty
3. Technologies Required
4. Short Description
5. Expected Learning Outcome

Keep the response under 300 words.
"""

    return generate_response(prompt)


# ==========================================================
# Interview Feedback
# ==========================================================

def generate_interview_feedback(question, answer):

    prompt = f"""
You are a Senior Technical Interviewer.

Interview Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer.

Provide:

1. Overall Score (/10)
2. Technical Accuracy
3. Communication Skills
4. Missing Concepts
5. Improvement Suggestions

Keep the response under 250 words.
"""

    return generate_response(prompt)