from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(score, strength, matched, missing, recommendations, filename):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>TalentMatch AI Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Resume Match Score:</b> {score}%", styles["Normal"]))
    story.append(Paragraph(f"<b>Resume Strength:</b> {strength}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/><b>AI Recommendations</b>", styles["Heading2"]))

    for rec in recommendations:
        story.append(Paragraph(f"• {rec}", styles["Normal"]))

    doc.build(story)
