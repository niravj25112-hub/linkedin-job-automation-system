from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.email import EmailMessage
from app.schemas.email import EmailMessageCreate, EmailMessageRead

router = APIRouter()


@router.get("/", response_model=list[EmailMessageRead])
def list_email_messages(db: Session = Depends(get_db)) -> list[EmailMessage]:
    return list(db.scalars(select(EmailMessage).order_by(EmailMessage.created_at.desc())).all())


@router.post("/", response_model=EmailMessageRead, status_code=201)
def create_email_message(
    payload: EmailMessageCreate, db: Session = Depends(get_db)
) -> EmailMessage:
    email_message = EmailMessage(**payload.model_dump())
    db.add(email_message)
    db.commit()
    db.refresh(email_message)
    return email_message


@router.post("/{email_message_id}/send")
def send_email_message(email_message_id: int) -> dict[str, int | str]:
    return {"email_message_id": email_message_id, "status": "queued"}

