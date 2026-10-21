
from sqlalchemy import CheckConstraint, Column, DateTime, UniqueConstraint, func, Integer, String, ForeignKey,Text
from app.database import Base

class JobVersion(Base):
    __tablename__ = "job_versions"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    version_number = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    location = Column(String, nullable=True)
    detailed_description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now()

    )

    __table_args__ = (
        UniqueConstraint("job_id", "version_number", name="uq_job_id_version_number"),
         CheckConstraint("version_number > 0", name="check_version_number_positive"),
    )
