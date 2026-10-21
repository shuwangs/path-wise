from sqlalchemy import Boolean,Column, Integer, String, DateTime, ForeignKey, UniqueConstraint, func
from app.database import Base
  
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    external_job_id = Column(String, nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)
    first_seen_at = Column(DateTime(timezone=True),nullable=False, server_default=func.now())
    last_checked_at = Column(DateTime(timezone=True),nullable=False, server_default=func.now())

    __table_args__ = (
        # Add a unique constraint on the combination of provider and board_token
        UniqueConstraint("source_id", "external_job_id", name="uq_source_id_external_job_id"),    
    )