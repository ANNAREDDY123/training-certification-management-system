from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.certificate import Certificate

from schemas.certificate import CertificateCreate

from services.training_service import (
    valid_certificate_dates
)

router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_certificate(
    certificate: CertificateCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Certificate).filter(
        Certificate.certificate_id == certificate.certificate_id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Certificate ID already exists."
        )

    if not valid_certificate_dates(
        certificate.issued_date,
        certificate.expiry_date
    ):

        raise HTTPException(
            status_code=400,
            detail="Expiry date must be after issued date."
        )

    new_certificate = Certificate(
        employee_id=certificate.employee_id,
        training_id=certificate.training_id,
        certificate_id=certificate.certificate_id,
        issued_date=certificate.issued_date,
        expiry_date=certificate.expiry_date
    )

    db.add(new_certificate)
    db.commit()
    db.refresh(new_certificate)

    return new_certificate


@router.get("/")
def get_certificates(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Certificate)

    total = query.count()

    certificates = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": certificates
    }


@router.get("/{certificate_id}")
def get_certificate(
    certificate_id: str,
    db: Session = Depends(get_db)
):

    certificate = db.query(Certificate).filter(
        Certificate.certificate_id == certificate_id
    ).first()

    if not certificate:

        raise HTTPException(
            status_code=404,
            detail="Certificate not found."
        )

    return certificate
