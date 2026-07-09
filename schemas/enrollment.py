from pydantic import BaseModel

from datetime import date


class EnrollmentCreate(BaseModel):

    employee_id: int

    training_id: int

    enrollment_date: date

    completion_status: str
