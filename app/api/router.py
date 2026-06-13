from fastapi import APIRouter

from app.api.routes import email, health, jobs, resumes, submissions

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(resumes.router, prefix="/resumes", tags=["resumes"])
api_router.include_router(email.router, prefix="/email", tags=["email"])
api_router.include_router(submissions.router, prefix="/submissions", tags=["submissions"])

