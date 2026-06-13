from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobRead

router = APIRouter()


@router.get("/", response_model=list[JobRead])
def list_jobs(db: Session = Depends(get_db)) -> list[Job]:
    return list(db.scalars(select(Job).order_by(Job.created_at.desc())).all())


@router.post("/", response_model=JobRead, status_code=201)
def create_job(payload: JobCreate, db: Session = Depends(get_db)) -> Job:
    job = Job(**payload.model_dump(mode="json"))
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@router.post("/search")
def search_jobs() -> dict[str, str]:
    return {"status": "queued", "message": "Job search service placeholder created."}

