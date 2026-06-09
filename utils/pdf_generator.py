from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    scores,
    filename="Interview_Report.pdf"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Interview Prep Bot Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    total = sum(scores)

    average = total / len(scores)

    elements.append(
        Paragraph(
            f"Average Score: {average:.1f}/10",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for i, score in enumerate(
        scores,
        start=1
    ):

        elements.append(
            Paragraph(
                f"Question {i}: {score}/10",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    if average >= 8:

        result = "Interview Ready"

    elif average >= 6:

        result = "Needs More Practice"

    else:

        result = "Focus on Fundamentals"

    elements.append(
        Paragraph(
            f"Recommendation: {result}",
            styles["Heading2"]
        )
    )

    doc.build(elements)

    return filename