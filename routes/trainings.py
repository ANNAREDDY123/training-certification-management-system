from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.training import Training

from schemas.training import TrainingCreate

from services.training_service import (
    valid_training_status,
    valid_training_dates
)

router = APIRouter(
    prefix="/trainings",
    tags=["Trainings"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_training(
    training: TrainingCreate,
    db: Session = Depends(get_db)
):

    if not valid_training_dates(
        training.start_date,
        training.end_date
    ):

        raise HTTPException(
            status_code=400,
            detail="Training end date must be after the start date."
        )

    if not valid_training_status(training.status):

        raise HTTPException(
            status_code=400,
            detail="Invalid training status."
        )

    new_training = Training(
        title=training.title,
        trainer_name=training.trainer_name,
        technology=training.technology,
        duration=training.duration,
        start_date=training.start_date,
        end_date=training.end_date,
        status=training.status
    )

    db.add(new_training)
    db.commit()
    db.refresh(new_training)

    return new_training


@router.get("/")
def get_trainings(
    technology: str = None,
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Training)

    if technology:
        query = query.filter(
            Training.technology.contains(technology)
        )

    if status:
        query = query.filter(
            Training.status == status
        )

    total = query.count()

    trainings = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": trainings
    }


@router.get("/{training_id}")
def get_training(
    training_id: int,
    db: Session = Depends(get_db)
):

    training = db.query(Training).filter(
        Training.id == training_id
    ).first()

    if not training:

        raise HTTPException(
            status_code=404,
            detail="Training not found."
        )

    return training


@router.put("/{training_id}")
def update_training(
    training_id: int,
    training: TrainingCreate,
    db: Session = Depends(get_db)
):

    db_training = db.query(Training).filter(
        Training.id == training_id
    ).first()

    if not db_training:

        raise HTTPException(
            status_code=404,
            detail="Training not found."
        )

    if not valid_training_dates(
        training.start_date,
        training.end_date
    ):

        raise HTTPException(
            status_code=400,
            detail="Training end date must be after the start date."
        )

    db_training.title = training.title
    db_training.trainer_name = training.trainer_name
    db_training.technology = training.technology
    db_training.duration = training.duration
    db_training.start_date = training.start_date
    db_training.end_date = training.end_date
    db_training.status = training.status

    db.commit()

    return {
        "message": "Training updated successfully."
    }


@router.delete("/{training_id}")
def delete_training(
    training_id: int,
    db: Session = Depends(get_db)
):

    training = db.query(Training).filter(
        Training.id == training_id
    ).first()

    if not training:

        raise HTTPException(
            status_code=404,
            detail="Training not found."
        )

    db.delete(training)
    db.commit()

    return {
        "message": "Training deleted successfully."
    }
