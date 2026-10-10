#  AI Incident & Log Analysis Assistant

A RESTful microservice built with **FastAPI** and **OpenAI API** that ingests raw server logs and error traces to generate automated Root-Cause Analysis (RCA) reports and actionable remediation steps.

##  Features
* **Automated Telemetry Analysis:** Parses complex system logs and stack traces.
* **Structured RCA Generation:** Produces concise summaries, root cause explanations, and mitigation steps.
* **Interactive API Documentation:** Native Swagger UI (`/docs`) for testing endpoints.

## Tech Stack
* **Framework:** FastAPI, Uvicorn
* **AI Provider:** OpenAI API (`gpt-4o-mini`)
* **Language:** Python 3.12+

## Getting Started

### 1. Clone & Setup Environment
```bash
git clone [https://github.com/THOMAS-SARAH/exception-analyzer.git](https://github.com/THOMAS-SARAH/exception-analyzer.git)
cd exception-analyzer
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Run Application
```bash
python -m uvicorn main:app --reload
```
Open `http://127.0.0.1:8000/docs` in your browser to interact with the API.
