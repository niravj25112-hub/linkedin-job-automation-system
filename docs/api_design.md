# API Design

## Base URL

All initial routes are under:

```text
/api/v1
```

## Health

### `GET /health`

Returns API status and environment.

## Jobs

### `GET /jobs`

Lists stored jobs, newest first.

### `POST /jobs`

Creates a job record.

### `POST /jobs/search`

Queues or triggers a recent job search. The starter implementation returns a placeholder response until the search integration is implemented.

## Resumes

### `GET /resumes`

Lists stored candidate resumes.

### `POST /resumes`

Creates a resume metadata record.

### `POST /resumes/{resume_id}/match`

Queues or triggers matching for one resume.

## Email

### `GET /email`

Lists generated email messages.

### `POST /email`

Creates a generated or drafted recruiter email.

### `POST /email/{email_message_id}/send`

Queues or triggers Gmail delivery.

## Submissions

### `GET /submissions`

Lists candidate submissions.

### `POST /submissions`

Creates a submission record linking a job, resume, recruiter email, match score, and status.

## Authentication Plan

JWT authentication will protect all workflow endpoints except `GET /health`. Initial implementation should add:

- User model and password hashing.
- Login route issuing access tokens.
- Dependency for current authenticated user.
- Role-aware authorization if multiple team members use the platform.

