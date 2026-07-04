import re


def analyze_resume(text):
    """
    Analyze resume and return:
    score,
    skills_found,
    education,
    experience
    """

    text = text.lower()

    # -----------------------------
    # Skills Database
    # -----------------------------

    all_skills = [
        "python",
        "java",
        "c++",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "pandas",
        "numpy",
        "statistics",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "streamlit",
        "flask",
        "git",
        "github",
        "docker",
        "api"
    ]

    skills_found = []

    for skill in all_skills:

        if skill in text:
            skills_found.append(skill.title())

    # -----------------------------
    # Education
    # -----------------------------

    education = "Not Found"

    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "bca",
        "mca",
        "bsc",
        "msc",
        "computer science"
    ]

    for edu in education_keywords:

        if edu in text:

            education = edu.upper()
            break

    # -----------------------------
    # Experience
    # -----------------------------

    experience = "Fresher"

    match = re.search(r'(\d+)\s+year', text)

    if match:
        experience = match.group(1) + " Years"

    # -----------------------------
    # Resume Score
    # -----------------------------

    score = 40

    score += len(skills_found) * 3

    if education != "Not Found":
        score += 10

    if experience != "Fresher":
        score += 10

    if score > 100:
        score = 100

    return (
        score,
        skills_found,
        education,
        experience
    )