from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl


class JobBase(BaseModel):
    title: str
    company: str | None = None
    location: str | None = None
    source_url: HttpUrl
    description: str | None = None
    keyword: str
    employment_type: str | None = None
    posted_at: datetime | None = None


class JobCreate(JobBase):
    pass


class JobRead(JobBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

