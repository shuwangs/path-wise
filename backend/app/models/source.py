"""Source model for the application."""

from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.database import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    provider = Column(String, nullable=False)
    board_token = Column(String, nullable=True, unique=True)
    created_at = Column(String, nullable=True)
    last_checked_at = Column(String, nullable=True)

    __table_args__ = (
        # Add a unique constraint on the combination of provider and board_token
        UniqueConstraint("provider", "board_token", name="uq_provider_board_token")    

    )