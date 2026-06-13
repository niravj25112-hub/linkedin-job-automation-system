from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class SubmissionBase(BaseModel):
    job_id: int
    resume_id: int
    recruiter_email: EmailStr | None = None
    match_score: float | None = None
    status: str = "pending"
    notes: str | None = None


class SubmissionCreate(SubmissionBase):
    pass


class SubmissionRead(SubmissionBase):
    id: int
    submitted_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

