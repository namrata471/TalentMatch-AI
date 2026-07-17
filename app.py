from flask import Flask, render_template, request, send_file
import os

from database import save_analysis, get_all_analysis
from utils.parser import extract_text
from utils.matcher import calculate_match_score
from utils.skill_extractor import extract_skills
from utils.pdf_generator import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Upload Resume
    resume = request.files["resume"]

    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(resume_path)

    # Extract Resume Text
    resume_text = extract_text(resume_path)

    # Read Job Description
    job_file = request.files["job_description"]
    job_text = job_file.read().decode("utf-8")

    # Calculate Match Score
    score = calculate_match_score(resume_text, job_text)

    # Resume Strength
    if score >= 80:
        strength = "Excellent 🟢"
    elif score >= 60:
        strength = "Good 🔵"
    elif score >= 40:
        strength = "Average 🟡"
    else:
        strength = "Needs Improvement 🔴"

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_text)

    # Matched Skills
    matched_skills = list(set(resume_skills) & set(jd_skills))

    # Missing Skills
    missing_skills = list(set(jd_skills) - set(resume_skills))

    # Recommendations
    recommendations = []

    if missing_skills:
        for skill in missing_skills:
            recommendations.append(f"Learn {skill}")
    else:
        recommendations.append(
            "Excellent! Your resume matches the job description well."
        )

    # Save analysis to SQLite
    candidate_name = os.path.splitext(resume.filename)[0]

    save_analysis(
        candidate_name,
        score,
        strength,
        matched_skills,
        missing_skills
    )

    # Generate PDF Report
    pdf_path = os.path.join(UPLOAD_FOLDER, "TalentMatch_Report.pdf")

    generate_pdf(
        score,
        strength,
        matched_skills,
        missing_skills,
        recommendations,
        pdf_path
    )

    return render_template(
        "result.html",
        score=score,
        strength=strength,
        matched=matched_skills,
        missing=missing_skills,
        recommendations=recommendations,
        matched_count=len(matched_skills),
        missing_count=len(missing_skills)
    )


@app.route("/download")
def download():
    pdf_path = os.path.join(UPLOAD_FOLDER, "TalentMatch_Report.pdf")
    return send_file(pdf_path, as_attachment=True)


@app.route("/dashboard")
def dashboard():

    data = get_all_analysis()

    return render_template(
        "dashboard.html",
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)
