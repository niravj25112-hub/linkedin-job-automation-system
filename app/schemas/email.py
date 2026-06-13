from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class EmailMessageBase(BaseModel):
    recipient_email: EmailStr
    subject: str
    body: str
    submission_id: int | None = None


class EmailMessageCreate(EmailMessageBase):
    pass


class EmailMessageRead(EmailMessageBase):
    id: int
    gmail_message_id: str | None = None
    status: str
    sent_at: datetime | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

