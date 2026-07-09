from pydantic import (
    BaseModel,
    Field
)

from datetime import date


class TrainingCreate(BaseModel):

    title: str = Field(..., min_length=3)

    trainer_name: str = Field(..., min_length=3)

    technology: str = Field(..., min_length=2)

    duration: str

    start_date: date

    end_date: date

    status: str
