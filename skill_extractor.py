def extract_skills(text):

    skills = [
        "Python",
        "SQL",
        "Flask",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Git",
        "GitHub",
        "Docker",
        "AWS",
        "Power BI",
        "Excel",
        "Java",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "Data Structures",
        "Algorithms"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills