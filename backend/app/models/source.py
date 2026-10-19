"""Source model for the application."""

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, func
from app.database import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    board_token = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),nullable=False, server_default=func.now())
    last_checked_at = Column(DateTime(timezone=True),nullable=True)

    __table_args__ = (
        # Add a unique constraint on the combination of provider and board_token
        UniqueConstraint("provider", "board_token", name="uq_provider_board_token"),    
    )