from docx import Document

document = Document()

document.add_heading(
    "ClearPath Health Technologies",
    level=1
)

document.add_paragraph("CareRoute Assist")
document.add_paragraph(
    "Supplemental Data Handling and Model Improvement Notes"
)
document.add_paragraph(
    "Synthetic document created for workflow testing only."
)

document.add_paragraph(
    "The following statements describe additional vendor practices:"
)

statements = [
    "Customer data may be retained in encrypted backup systems for up to 90 days after contract termination before full backup rotation is completed.",
    "Production data is not intentionally used to train foundation models.",
    "De-identified or aggregated customer-derived data may be used for internal model evaluation, performance tuning, and product improvement.",
    "Human staff review selected AI-generated recommendations, but not every recommendation requires manual review before downstream action.",
    "Encryption keys are vendor-managed. Key rotation schedules and hardware security module usage are not documented in this supplemental note.",
    "If there is a conflict between this supplemental note and other vendor documentation, this supplemental note should be treated as the most current description of vendor practices."
]

for statement in statements:
    document.add_paragraph(
        statement,
        style="List Bullet"
    )

document.save(
    "ClearPath_Conflicting_Evidence.docx"
)

print(
    "Created: ClearPath_Conflicting_Evidence.docx"
)