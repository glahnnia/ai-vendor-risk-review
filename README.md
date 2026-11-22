# AI Vendor Risk & Technology Due-Diligence Workflow

## Overview

The **AI Vendor Risk & Technology Due-Diligence Workflow** is a prototype decision-support application designed to help reviewers evaluate technology and AI vendors using structured, evidence-grounded analysis.

The application reviews vendor-supplied documentation for material privacy, security, AI-governance, regulatory, operational, and documentation-integrity concerns. It can analyze multiple documents together, identify substantive contradictions between sources, generate targeted follow-up questions, and produce structured materials for human review.

The system is explicitly designed **not to autonomously approve or reject vendors**. Final risk interpretation, escalation, acceptance, and contracting decisions remain with human reviewers.

---

## Current Implementation

The current version is implemented locally using:

- **Python 3.12**
- **OpenAI Agents SDK**
- **Pydantic structured output**
- **Streamlit**
- **PyPDF**
- **python-docx**
- **ReportLab**

The application currently supports:

- TXT files
- PDFs containing extractable text
- DOCX files
- Multiple documents in a single vendor review
- Partial document-processing failures
- Source-aware evidence analysis
- Cross-document contradiction detection
- Structured JSON output
- Standalone PDF report generation
- Mandatory human-review requirements

---

## Core Workflow

The workflow follows this sequence:

### 1. Vendor Intake

The reviewer enters:

- Vendor name
- Product name

### 2. Document Upload

The reviewer uploads one or more vendor documents in supported formats:

- TXT
- PDF
- DOCX

### 3. Document Validation

Each document is checked for:

- Supported file type
- File accessibility
- Readable content

Unreadable, missing, or unsupported documents are identified separately.

AI analysis proceeds only when at least one usable document remains.

### 4. Text Extraction

The application extracts:

- TXT content directly
- PDF text page by page
- DOCX paragraphs and tables

Source filenames remain associated with extracted evidence.

### 5. Untrusted-Document Boundary

Vendor documentation is explicitly treated as **untrusted input**.

Embedded instructions inside uploaded documents cannot override:

- The analyst role
- Required output structure
- Risk-review safeguards
- Human decision authority

### 6. AI-Assisted Vendor Risk Analysis

The OpenAI Agents SDK analyzes the combined evidence packet.

The workflow is instructed to:

- Distinguish vendor claims from verified evidence
- Avoid inventing certifications, controls, or safeguards
- Treat missing information as unknown
- Give affirmative evidence appropriate weight
- Focus findings on materially relevant concerns
- Keep analysis proportional to the supplied evidence

### 7. Cross-Document Conflict Detection

The workflow identifies materially inconsistent statements across vendor documents.

For each genuine conflict, it preserves:

- Topic
- Source documents
- Competing claims
- Explanation
- Human-resolution requirement

The application does not silently reconcile conflicting statements or automatically determine which vendor document is authoritative.

### 8. Structured Output

The system returns:

- Vendor and product information
- Evidence observed
- Risk findings
- Uncertainties
- Document conflicts
- Follow-up questions
- Human-review requirement
- Human-review notes

### 9. Reviewer Output

Results are displayed through the Streamlit interface.

Reviewers can download:

- Structured JSON
- Standalone human-readable PDF report

---

## Human-in-the-Loop Design

Human decision authority is a foundational workflow requirement.

The application:

- Does not approve vendors
- Does not reject vendors
- Requires human review for every analysis
- Separates vendor claims from validated evidence
- Identifies unresolved conflicts instead of resolving them automatically
- Generates targeted follow-up questions
- Preserves escalation and risk-acceptance decisions for human reviewers

AI-generated findings are therefore treated as **decision-support information**, not final vendor-risk determinations.

---

## Evidence and Risk Calibration Safeguards

### Evidence Grounding

The model is instructed to:

- Distinguish vendor claims from verified evidence
- Avoid inventing safeguards, certifications, controls, or facts
- Give affirmative evidence appropriate weight
- Treat missing information as unknown
- Avoid assuming undocumented controls are absent
- Base findings on evidence present in the supplied record

### Risk Calibration

The workflow is designed to:

- Avoid manufacturing findings merely because every conceivable technical detail was not supplied
- Distinguish inherent risk from evidence of a vendor control deficiency
- Keep review proportional to available evidence
- Limit risk findings and follow-up questions to material issues
- Avoid assuming applicability of HIPAA, PHI, BAAs, SOC 2, ISO 27001, or similar requirements without supporting evidence

### Document Safety and Prompt-Injection Resistance

Vendor documentation is treated as untrusted input.

The model is instructed to ignore embedded content attempting to:

- Change the analyst role
- Suppress findings
- Force vendor approval
- Alter required output
- Override human decision authority
- Request hidden instructions
- Manipulate interpretation of other documents

Potential prompt-injection or documentation-integrity concerns are summarized rather than blindly reproduced.

---

## Development History

### Phase 1: n8n Prototype

The project began as an n8n workflow combining deterministic routing, OpenAI-based risk analysis, structured outputs, and a human-review stage.

Synthetic vendor scenarios were used throughout development so workflow behavior could be tested without confidential vendor information.

Testing evaluated:

- Documentation routing
- Structured-output reliability
- Evidence grounding
- Anti-fabrication behavior
- Ambiguous information
- Conflicting vendor evidence
- Regulatory-language precision
- Prompt-injection resistance
- Human decision safeguards
- Risk calibration
- False-positive resistance
- Regression behavior following prompt refinements

The testing process resulted in iterative improvements to evidence handling, contradiction detection, prompt-injection safeguards, and risk calibration.

### Phase 2: n8n Implementation

The prototype was expanded with:

- Vendor intake
- Normalization
- Multi-document processing
- Source attribution
- Document-quality routing
- Partial document-processing failure handling

The n8n Cloud implementation was later moved to a locally hosted Docker environment in an effort to continue development without ongoing cloud-platform AI-credit consumption.

While vendor intake and document-processing logic worked locally, AI execution became blocked by an n8n integration/licensing issue. Continued troubleshooting would have introduced disproportionate implementation overhead.

The validated prompts, schemas, safeguards, test scenarios, and workflow architecture were therefore retained while the project migrated away from n8n.

### Phase 3: Native Python/OpenAI Implementation

The workflow was rebuilt as a local Python application using the OpenAI Agents SDK.

The Python implementation added:

- Native OpenAI Agents SDK execution
- Pydantic structured outputs
- TXT processing
- PDF processing
- DOCX processing
- Multiple-document analysis
- Source preservation
- Cross-document contradiction detection
- Missing and unreadable-document handling
- Partial-failure processing
- JSON report generation
- Streamlit user interface
- Human-readable DOCX reporting during development
- Standalone PDF report generation using ReportLab

Cross-format regression testing confirmed that equivalent TXT, PDF, and DOCX evidence packets continued to produce the intended material document conflicts.

---

## Current Application Architecture

```text
Reviewer
   ↓
Streamlit Vendor Intake
   ↓
Multi-Document Upload
   ↓
Document Type Validation
   ↓
TXT / PDF / DOCX Extraction
   ↓
Document Quality Routing
   ↓
Source-Attributed Evidence Packet
   ↓
Untrusted Content Boundary
   ↓
OpenAI Agents SDK Risk Analyst
   ↓
Pydantic Structured Output
   ↓
Conflict Detection + Human Review
   ↓
Streamlit Review Interface
   ↓
JSON Report + PDF Report
```

---

## Validated Test Behaviors

Testing has confirmed that the workflow can:

- Process a single valid vendor document
- Process multiple vendor documents
- Continue analysis when some documents fail but usable documents remain
- Stop analysis when no usable documents remain
- Handle missing-file conditions
- Extract TXT content
- Extract PDF text
- Extract DOCX paragraphs and tables
- Preserve source filenames during analysis
- Detect material contradictions between documents
- Distinguish contradictions from ordinary differences in detail
- Preserve human decision authority
- Produce structured JSON output
- Produce a downloadable standalone PDF review report
- Operate through a browser-based Streamlit interface

---

## Example Conflict-Detection Test

A synthetic **ClearPath Health Technologies / CareRoute Assist** evidence packet was used to validate cross-document analysis.

The workflow identified three material conflicts involving:

### 1. Post-Termination Data Retention

One source states that production data is deleted within 30 days after contract termination, while supplemental documentation allows encrypted backup retention for up to 90 days.

### 2. Human Review of AI Recommendations

One source describes human review before action, while another states that only selected AI-generated recommendations receive manual review.

### 3. Customer Data and Model Improvement

One source states that customer data is not used to train foundation models, while supplemental documentation allows de-identified or aggregated customer-derived data to be used for evaluation, performance tuning, and product improvement.

The workflow preserved the competing claims and routed them for human resolution rather than selecting one source as automatically authoritative.

---

## Final Regression Test

A final end-to-end regression test was completed using the synthetic **ClearPath Health Technologies / CareRoute Assist** evidence packet.

The test processed:

- `ClearPath_Test_Security_Overview.txt`
- A generated `ClearPath_Conflicting_Evidence.docx` fixture

The DOCX fixture can be recreated using:

```text
create_test_docx.py
```

A PDF version of the conflicting-evidence fixture is also included in this repository for demonstration and review.

Final intake results:

- **Documents submitted:** 2
- **Documents successfully processed:** 2
- **Documents failed:** 0

The workflow successfully:

- Preserved source attribution
- Identified expected material conflicts
- Generated targeted follow-up questions
- Maintained mandatory human decision authority
- Produced structured JSON output
- Produced a standalone PDF report

The prototype is considered functionally complete for its intended local demonstration and portfolio use.

---

## Example Outputs

### Structured Vendor Risk Review

`clearpath_health_technologies_vendor_risk_review.json`

Demonstrates a completed multi-document analysis containing:

- Evidence observations
- Risk findings
- Uncertainties
- Document conflicts
- Follow-up questions
- Human-review notes
- Document intake metadata

### Document Intake Failure

`clearpath_health_technologies_document_intake_failure.json`

Demonstrates safe failure handling when no usable vendor document is available.

In this scenario, the workflow:

- Identifies the missing document
- Records the intake failure
- Does not run the AI risk analysis
- Produces a structured failure record

### Human-Readable PDF Report

`clearpath_health_technologies_vendor_risk_review.pdf`

Demonstrates the standalone reviewer-facing report generated from the structured analysis.

The report includes:

- Vendor information
- Review scope
- Document intake summary
- Evidence observed
- Risk findings
- Uncertainties
- Cross-document conflicts
- Follow-up questions
- Human-review requirements

---

## Streamlit Interface

The repository includes screenshots demonstrating the browser-based workflow:

- `AI Vendor Risk Review_Streamlit interface_Screenshot 1.png`
- `AI Vendor Risk Review_Streamlit interface_Screenshot 2.png`
- `AI Vendor Risk Review_Streamlit interface_Screenshot 3.png`
- `AI Vendor Risk Review_Streamlit interface_Screenshot 4.png`
- `AI Vendor Risk Review_Streamlit interface_Screenshot 5.png`
- `AI Vendor Risk Review_Streamlit interface_Screenshot 6.png`

These screenshots document the working interface from vendor intake through review results and downloadable outputs.

---

## Repository Contents

```text
ai-vendor-risk-review/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── ClearPath_Test_Security_Overview.txt
├── ClearPath_Conflicting_Evidence.pdf
├── create_test_docx.py
│
├── clearpath_health_technologies_document_intake_failure.json
├── clearpath_health_technologies_vendor_risk_review.json
├── clearpath_health_technologies_vendor_risk_review.pdf
│
├── AI Vendor Risk Review_Streamlit interface_Screenshot 1.png
├── AI Vendor Risk Review_Streamlit interface_Screenshot 2.png
├── AI Vendor Risk Review_Streamlit interface_Screenshot 3.png
├── AI Vendor Risk Review_Streamlit interface_Screenshot 4.png
├── AI Vendor Risk Review_Streamlit interface_Screenshot 5.png
└── AI Vendor Risk Review_Streamlit interface_Screenshot 6.png
```

### Key Files

**`app.py`**  
Primary Streamlit application containing the browser-based vendor intake, document processing, AI analysis, structured output, and downloadable report workflow.

**`main.py`**  
Command-line implementation of the vendor-risk analysis workflow used during development and testing.

**`create_test_docx.py`**  
Utility for generating the synthetic DOCX evidence fixture used in cross-format testing.

**Synthetic ClearPath files**  
Test documents created specifically for workflow validation. They do not contain confidential vendor information.

**JSON outputs**  
Demonstrate both successful structured risk analysis and safe intake-failure handling.

**PDF output**  
Demonstrates the final human-readable vendor-risk report.

**Streamlit screenshots**  
Provide visual documentation of the completed interface and workflow.

---

## Known Limitations

The application remains a prototype.

Current limitations include:

- PDF processing relies on extractable embedded text and does not provide OCR for image-only scanned PDFs
- AI output may exhibit some run-to-run variation
- Vendor statements are not independently verified merely because they appear in uploaded documentation
- Human reviewers remain responsible for validating relevant technical, contractual, audit, regulatory, and organizational evidence
- The application currently runs locally
- Enterprise authentication is not implemented
- Persistent database storage is not implemented
- Formal reviewer authorization and role-based access controls are not implemented
- Production audit logging is not implemented

---

## Privacy and Data Handling

Development and testing use **synthetic vendor records**.

The ClearPath Health Technologies / CareRoute Assist materials included in this repository were created specifically for workflow testing and portfolio demonstration.

Real confidential vendor documentation should not be introduced without an appropriate:

- Organizational data-handling policy
- API configuration
- Security review
- Authorization process

API credentials should never be embedded directly in application source code or committed to version control.

---

## Installation

Create and activate a Python virtual environment, then install the required packages:

```powershell
pip install -r requirements.txt
```

Required dependencies are documented in `requirements.txt`.

---

## Running the Application

Set the OpenAI API key in the local environment.

Then launch the Streamlit interface:

```powershell
streamlit run app.py
```

If necessary:

```powershell
python -m streamlit run app.py
```

The application will open locally in a web browser.

---

## Intended Use

This project demonstrates an approach to combining:

- AI-assisted analysis
- Vendor due diligence
- Privacy and security review
- AI governance
- Evidence grounding
- Document-processing pipelines
- Structured outputs
- Cross-document conflict detection
- Prompt-injection safeguards
- Human-in-the-loop decision systems
- Automated report generation

It is intended as a **prototype and portfolio demonstration**, not an autonomous vendor-approval system.

---

## Status

**Current status: End-to-end prototype complete and final regression testing passed.**

The completed application supports:

- Browser-based vendor and product intake
- Multi-document upload and review
- TXT, PDF, and DOCX document processing
- Document intake validation and partial-failure handling
- Source-aware evidence analysis
- Prompt-injection and untrusted-document safeguards
- Cross-document contradiction detection
- Structured Pydantic output
- Mandatory human-review routing
- Structured JSON export
- Standalone PDF report generation
- Portfolio-ready Streamlit workflow documentation

### Future Enhancements

Potential future enhancements include:

- Secure hosted deployment
- Authentication
- Persistent review history
- Expanded OCR support
- Audit logging
- Role-based reviewer controls
- Enterprise governance integrations
- Additional document formats
- Formal evaluation datasets
- Automated regression testing
    
---

## Project Significance

This project demonstrates how applied AI, structured document processing, and evidence-based analysis can support technology vendor due diligence.

By combining multi-document analysis, source attribution, contradiction detection, structured reporting, and mandatory human oversight, the workflow illustrates how AI can strengthen organizational risk-review processes without replacing human decision-making.

The project also demonstrates practical experience in AI governance, agent-based workflows, document-processing pipelines, prompt-injection safeguards, and automated reporting.

---

**Project Type:** Applied AI Governance & Technology Risk Assessment Portfolio Project  
**Technologies:** Python 3.12, OpenAI Agents SDK, Pydantic, Streamlit, PyPDF, python-docx, ReportLab  
**Data Classification:** Synthetic Vendor Documentation / Demonstration Data  
**Implementation:** Local Functional Prototype  
**Project Status:** End-to-End Prototype Complete; Regression Testing Passed  

**Developed by Glahnnia "Renee" Rates, MSHS, CCHW II**  
Public Health Informatics | Applied AI | Workforce Development | Data Analytics

