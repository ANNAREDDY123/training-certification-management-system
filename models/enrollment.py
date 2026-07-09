from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from database import Base


class Enrollment(Base):

    __tablename__ = "enrollments"

    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(Integer)

    training_id = Column(
        Integer,
        ForeignKey("trainings.id")
    )

    enrollment_date = Column(Date)

    completion_status = Column(String)
