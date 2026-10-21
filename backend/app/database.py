"""Database engine and session lifecycle."""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import DATABASE_URL


class Base(DeclarativeBase):
    pass

# the start of SQLAlchemy is an OBJ call engined.
# as center souce for connections to particular db.
# DB enginer
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 3},
)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db() -> Generator[Session, None, None]:
    """Provide one session per request and always close it."""
    with SessionLocal() as session:
        yield session
