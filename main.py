import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.trainings import router as trainings_router
from routes.enrollments import router as enrollments_router
from routes.certificates import router as certificates_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Training & Certification Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(trainings_router)
app.include_router(enrollments_router)
app.include_router(certificates_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "Training & Certification Management System"
    }
