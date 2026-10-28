"""Implement database transaction management using SQLAlchemy."""

from sqlalchemy.orm import Session

from app.interfaces.unit_of_work import IUnitOfWork


class SqlAlchemyUnitOfWork(IUnitOfWork):
    """
    Manage database transactions through SQLAlchemy.

    Uses an injected session shared with repositories.
    The session lifecycle is managed externally.
    """

    def __init__(self, db: Session) -> None:
        """
        Initialize the Unit of Work.

        Args:
            db: SQLAlchemy session shared with repositories.
        """
        self.db = db

    def commit(self) -> None:
        """
        Commit the current database transaction.

        SQLAlchemy flushes pending changes automatically
        before committing.
        """
        self.db.commit()

    def rollback(self) -> None:
        """
        Roll back the current database transaction.

        Discards database changes that have not
        been committed.
        """
        self.db.rollback()
