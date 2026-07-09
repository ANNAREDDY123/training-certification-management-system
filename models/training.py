from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)

from database import Base


class Training(Base):

    __tablename__ = "trainings"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(String)

    trainer_name = Column(String)

    technology = Column(String)

    duration = Column(String)

    start_date = Column(Date)

    end_date = Column(Date)

    status = Column(String)
