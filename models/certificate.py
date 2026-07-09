from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from database import Base


class Certificate(Base):

    __tablename__ = "certificates"

    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(Integer)

    training_id = Column(
        Integer,
        ForeignKey("trainings.id")
    )

    certificate_id = Column(
        String,
        unique=True
    )

    issued_date = Column(Date)

    expiry_date = Column(Date)
