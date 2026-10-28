"""Configure the SQLAlchemy database engine and sessions."""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models."""


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session for a request.

    Yields:
        An SQLAlchemy session.

    Notes:
        The session is closed automatically when
        the dependency finishes. Transaction commits
        are managed by the Unit of Work.
    """
    with SessionLocal() as db:
        yield db
