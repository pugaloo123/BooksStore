from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None


class BookCreate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True
