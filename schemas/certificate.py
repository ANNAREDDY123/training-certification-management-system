from pydantic import (
    BaseModel,
    Field
)

from datetime import date


class CertificateCreate(BaseModel):

    employee_id: int

    training_id: int

    certificate_id: str = Field(..., min_length=5)

    issued_date: date

    expiry_date: date
