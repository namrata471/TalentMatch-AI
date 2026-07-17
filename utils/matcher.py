import re

def calculate_match_score(resume_text, job_text):

    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    job_words = set(re.findall(r'\b\w+\b', job_text.lower()))

    common_words = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0

    score = (len(common_words) / len(job_words)) * 100

    return round(score, 2)
