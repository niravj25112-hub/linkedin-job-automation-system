from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.submission import Submission
from app.schemas.submission import SubmissionCreate, SubmissionRead

router = APIRouter()


@router.get("/", response_model=list[SubmissionRead])
def list_submissions(db: Session = Depends(get_db)) -> list[Submission]:
    return list(db.scalars(select(Submission).order_by(Submission.created_at.desc())).all())


@router.post("/", response_model=SubmissionRead, status_code=201)
def create_submission(payload: SubmissionCreate, db: Session = Depends(get_db)) -> Submission:
    submission = Submission(**payload.model_dump())
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission

