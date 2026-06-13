# Development Roadmap

## Phase 1: Foundation

- Add Alembic database migrations.
- Add user model and JWT login routes.
- Add request validation and error handling conventions.
- Add service-level unit tests.

## Phase 2: Job Discovery

- Implement job-source adapter interfaces.
- Add recent-job search by configured keyword filters.
- Normalize and deduplicate job records by source URL.
- Add scheduled search execution.

## Phase 3: Resume Processing

- Add resume upload endpoint.
- Parse PDF and DOCX resumes into text.
- Extract candidate skills and contact metadata.
- Store parsed resume content for matching.

## Phase 4: Matching

- Improve scoring with weighted keywords, title matching, location, and C2C indicators.
- Store match results and explanations.
- Add APIs to review top candidate-job matches.

## Phase 5: Gmail Integration

- Implement Gmail OAuth flow.
- Store encrypted token metadata.
- Send recruiter emails with resume attachments.
- Track Gmail message IDs and send timestamps.

## Phase 6: Submission Tracking

- Add submission lifecycle statuses.
- Add follow-up reminders.
- Add recruiter response tracking.
- Add dashboard-ready aggregate endpoints.

## Phase 7: Production Readiness

- Add Docker Compose for API and PostgreSQL.
- Add structured logging.
- Add background worker infrastructure.
- Add CI checks for tests, linting, and type checks.
- Add deployment documentation.

