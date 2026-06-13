# Project Architecture

## Overview

The LinkedIn Job Automation System is a FastAPI backend that coordinates recruitment automation workflows from job discovery to candidate submission tracking.

## Components

### API Layer

The `app/api` package exposes versioned FastAPI routes. Route modules are intentionally grouped by business area:

- `health.py` for operational health checks.
- `jobs.py` for job storage and search triggers.
- `resumes.py` for candidate resume records and matching triggers.
- `email.py` for generated recruiter emails and Gmail send triggers.
- `submissions.py` for tracking candidate submissions.

### Service Layer

The `app/services` package contains business logic:

- `JobSearchService` will coordinate provider-specific job searches and keyword filtering.
- `ResumeMatchingService` computes fit between resumes and job descriptions.
- `EmailService` generates recruiter messages and will wrap Gmail API delivery.
- `SubmissionService` centralizes submission status behavior.

### Persistence Layer

The `app/models` package contains SQLAlchemy ORM models backed by PostgreSQL:

- `Job`
- `Resume`
- `EmailMessage`
- `Submission`

The database engine and sessions live in `app/database`.

### Core Configuration

The `app/core` package contains application settings and security helpers. Settings load from environment variables and `.env`.

## Data Flow

1. A job search is triggered for configured C2C keyword filters.
2. Matching jobs are stored in PostgreSQL.
3. Candidate resumes are uploaded, parsed, and stored.
4. Matching calculates candidate fit for each relevant job.
5. Recruiter emails are generated from job and candidate context.
6. Gmail API sends the message.
7. Submission and email statuses are tracked for follow-up.

## External Integrations

- PostgreSQL for relational persistence.
- Gmail API for authenticated sending.
- Job-search source integrations will be added behind the service layer.

