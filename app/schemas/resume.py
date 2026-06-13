from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class ResumeBase(BaseModel):
    candidate_name: str
    candidate_email: EmailStr | None = None
    file_path: str
    parsed_text: str | None = None
    skills: str | None = None


class ResumeCreate(ResumeBase):
    pass


class ResumeRead(ResumeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

