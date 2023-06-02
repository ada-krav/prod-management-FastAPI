from datetime import datetime
from typing import List
from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    id: str | None = None
    name: str
    description: str
    price: float
    createdAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]

