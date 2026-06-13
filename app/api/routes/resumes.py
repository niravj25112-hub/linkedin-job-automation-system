from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate, ResumeRead

router = APIRouter()


@router.get("/", response_model=list[ResumeRead])
def list_resumes(db: Session = Depends(get_db)) -> list[Resume]:
    return list(db.scalars(select(Resume).order_by(Resume.created_at.desc())).all())


@router.post("/", response_model=ResumeRead, status_code=201)
def create_resume(payload: ResumeCreate, db: Session = Depends(get_db)) -> Resume:
    resume = Resume(**payload.model_dump())
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


@router.post("/{resume_id}/match")
def match_resume(resume_id: int) -> dict[str, int | str]:
    return {"resume_id": resume_id, "status": "queued"}

