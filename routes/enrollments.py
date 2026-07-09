from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.enrollment import Enrollment
from models.training import Training

from schemas.enrollment import EnrollmentCreate

from services.training_service import (
    valid_completion_status
)

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):

    training = db.query(Training).filter(
        Training.id == enrollment.training_id
    ).first()

    if not training:

        raise HTTPException(
            status_code=404,
            detail="Training not found."
        )

    duplicate = db.query(Enrollment).filter(
        Enrollment.employee_id == enrollment.employee_id,
        Enrollment.training_id == enrollment.training_id
    ).first()

    if duplicate:

        raise HTTPException(
            status_code=400,
            detail="Employee is already enrolled in this training."
        )

    if not valid_completion_status(
        enrollment.completion_status
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid completion status."
        )

    new_enrollment = Enrollment(
        employee_id=enrollment.employee_id,
        training_id=enrollment.training_id,
        enrollment_date=enrollment.enrollment_date,
        completion_status=enrollment.completion_status
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment


@router.get("/")
def get_enrollments(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Enrollment)

    total = query.count()

    enrollments = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": enrollments
    }


@router.get("/employees/{employee_id}/trainings")
def employee_trainings(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Enrollment).filter(
        Enrollment.employee_id == employee_id
    ).all()


@router.put("/{enrollment_id}")
def update_enrollment(
    enrollment_id: int,
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):

    db_enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if not db_enrollment:

        raise HTTPException(
            status_code=404,
            detail="Enrollment not found."
        )

    if db_enrollment.completion_status == "Completed":

        raise HTTPException(
            status_code=400,
            detail="Completed enrollments cannot be modified."
        )

    db_enrollment.completion_status = enrollment.completion_status

    db.commit()

    return {
        "message": "Enrollment updated successfully."
    }
