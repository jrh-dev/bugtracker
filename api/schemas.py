from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    #id: int
    first: str
    last: str

    class Config:
        orm_mode = True

class UserGet(UserBase):
    id: int
    first: str
    last: str

    class Config:
        orm_mode = True

class BugBase(BaseModel):
    #id: int
    title: str
    description: str
    is_open: bool
    owner_id: int
    #time_created: datetime

    class Config:
        orm_mode = True

class BugGet(BugBase):
    id: int
    title: str
    description: str
    is_open: bool
    owner_id: int
    time_created: datetime

    class Config:
        orm_mode = True


class BugUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_open: Optional[bool] = None
    owner_id: Optional[int] = None

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    first: Optional[str] = None
    last: Optional[str] = None

    class Config:
        orm_mode = True
