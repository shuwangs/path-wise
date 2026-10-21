"""PathWise's minimal local API."""
import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()


app = FastAPI(title="PathWise API", version="0.1.0", lifespan=lifespan)
origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000,"
        "http://localhost:3001,http://127.0.0.1:3001"
    ).split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=[],
)


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health() -> HealthResponse:
    """Report process health; this does not check a database or external sources."""
    return HealthResponse(status="ok", service="pathwise-api")


@app.get("/ready", response_model=HealthResponse, tags=["health"])
def ready(db: Session = Depends(get_db)) -> HealthResponse:
    """Check database connectivity without exposing connection details."""
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable") from None
    return HealthResponse(status="ok", service="pathwise-api")
