import sqlite3


def create_database():
    conn = sqlite3.connect("talentmatch.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_name TEXT,
            score REAL,
            strength TEXT,
            matched_skills TEXT,
            missing_skills TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(candidate_name, score, strength, matched_skills, missing_skills):

    conn = sqlite3.connect("talentmatch.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resume_analysis
        (candidate_name, score, strength, matched_skills, missing_skills)
        VALUES (?, ?, ?, ?, ?)
    """, (
        candidate_name,
        score,
        strength,
        ", ".join(matched_skills),
        ", ".join(missing_skills)
    ))

    conn.commit()
    conn.close()

def get_all_analysis():
    conn = sqlite3.connect("talentmatch.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM resume_analysis
        ORDER BY score DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
if __name__ == "__main__":
    create_database()
    print("Database Created Successfully!")
