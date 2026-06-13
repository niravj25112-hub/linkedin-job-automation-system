# LinkedIn Job Automation System

A FastAPI backend for recruitment automation workflows: job discovery, C2C keyword filtering, resume matching, recruiter email generation, Gmail delivery, and submission tracking.

## Goals

- Search for recent job opportunities.
- Filter target roles by:
  - Java Developer + C2C
  - Business Analyst + C2C
  - Project Manager + C2C
  - Data Analyst + C2C
- Store job, resume, email, and submission data in PostgreSQL.
- Match candidate resumes against job descriptions.
- Generate recruiter outreach emails.
- Send emails through the Gmail API.
- Track submission status from draft through sent and follow-up.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT authentication
- Gmail API

## Project Structure

```text
linkedin-job-automation-system/
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   ├── database/
│   ├── core/
│   └── utils/
├── docs/
├── tests/
├── resumes/
├── scripts/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── main.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Update `.env` with your PostgreSQL connection string, JWT secret, and Gmail OAuth credentials.

## Database

Create the PostgreSQL database, then run:

```bash
python scripts/create_tables.py
```

## Run the API

```bash
uvicorn main:app --reload
```

Open:

- API: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/api/v1/health`

## Current Starter Endpoints

- `GET /api/v1/health`
- `GET /api/v1/jobs`
- `POST /api/v1/jobs`
- `POST /api/v1/jobs/search`
- `GET /api/v1/resumes`
- `POST /api/v1/resumes`
- `POST /api/v1/resumes/{resume_id}/match`
- `GET /api/v1/email`
- `POST /api/v1/email`
- `POST /api/v1/email/{email_message_id}/send`
- `GET /api/v1/submissions`
- `POST /api/v1/submissions`

## Development Status

This repository is initialized with a professional backend structure and starter code. The next major work areas are migrations, authentication, real job-source integrations, resume parsing, Gmail OAuth, background jobs, and tests around the matching and submission workflows.

