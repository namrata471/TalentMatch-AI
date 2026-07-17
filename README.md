# TalentMatch AI – Intelligent Resume Screening System

## Overview

TalentMatch AI is an AI-powered Resume Screening System that helps recruiters compare resumes against job descriptions. The application analyzes resumes, calculates a match score using Natural Language Processing (NLP), identifies matched and missing skills, generates recommendations, stores candidate analyses in a SQLite database, and produces downloadable PDF reports.

---

## Features

* Upload Resume (PDF)
* Upload Job Description (.txt)
* AI-based Resume Match Score
* Resume Strength Analysis
* Matched Skills Detection
* Missing Skills Identification
* AI Recommendations
* Skill Analysis Pie Chart
* Downloadable PDF Report
* Recruiter Dashboard
* SQLite Database for Candidate Records

---

## Technologies Used

### Programming Language

* Python

### Backend

* Flask

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite

### AI & NLP

* TF-IDF Vectorization
* Cosine Similarity
* Rule-Based Skill Extraction

### Libraries

* Scikit-learn
* PyPDF2 / PDF parser
* Matplotlib
* ReportLab

---

## Project Structure

```text
TalentMatch-AI/
│
├── app.py
├── database.py
├── requirements.txt
├── templates/
├── utils/
├── static/
├── uploads/
└── README.md
```

---

## How It Works

1. Upload a resume in PDF format.
2. Upload a job description in TXT format.
3. The system extracts text from the resume.
4. TF-IDF converts the resume and job description into numerical vectors.
5. Cosine Similarity calculates the resume match score.
6. The system extracts skills from both documents.
7. Matched and missing skills are identified.
8. AI recommendations are generated.
9. Results are displayed on the web application.
10. The analysis is stored in SQLite and can be viewed in the Recruiter Dashboard.
11. A PDF report can be downloaded.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/TalentMatch-AI.git
```

Navigate to the project folder:

```bash
cd TalentMatch-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Screenshots

Add screenshots here after uploading your project.

* Home Page
* Resume Analysis Report
* Recruiter Dashboard

---

## Future Enhancements

* DOCX Resume Support
* PDF Job Description Support
* Advanced NLP using spaCy
* Candidate Search and Filters
* Dashboard Analytics
* Export to Excel
* Cloud Deployment
* User Authentication

---

## Author

**Namrata S. Balekundri**

Electronics & Communication Engineering Student

Interested in Software Development, AI, Data Analytics, and Machine Learning.

---

## License

This project is intended for educational and portfolio purposes.
