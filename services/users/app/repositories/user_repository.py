"""Implement user repository operations using SQLAlchemy."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.interfaces.user_repository import IUserRepository
from app.models.user import User


class UserRepository(IUserRepository):
    """
    SQLAlchemy implementation of the user repository.

    Provides CRUD operations for User entities using
    an injected database session.

    Transaction commits and rollbacks are managed by
    the calling layer.
    """

    def __init__(self, db: Session) -> None:
        """
        Initialize the repository.

        Args:
            db: SQLAlchemy session used for database operations.
        """
        self.db = db

    def get_all(self) -> list[User]:
        """
        Retrieve all users from the database.

        Returns:
            A list of User instances, or an empty list
            if no users exist.
        """
        statement = select(User).order_by(User.id)
        return list(self.db.scalars(statement).all())

    def get_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by their unique identifier.

        Args:
            user_id: Unique identifier of the user.

        Returns:
            The matching User instance, or None if not found.
        """
        statement = select(User).where(User.id == user_id)
        return self.db.scalar(statement)

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by their email address.

        Args:
            email: Email address to search for.

        Returns:
            The matching User instance, or None if not found.
        """
        statement = select(User).where(User.email == email)
        return self.db.scalar(statement)

    def create(self, user: User) -> User:
        """
        Add a new user and flush pending changes.

        Flushing executes pending SQL statements without
        committing the transaction.

        Args:
            user: User entity to create.

        Returns:
            The User instance with generated values
            available after flushing.

        Raises:
            sqlalchemy.exc.IntegrityError:
                If a database constraint is violated.
        """
        self.db.add(user)
        self.db.flush()

        return user

    def update(self, user: User) -> User:
        """
        Flush changes made to a session-managed user.

        SQLAlchemy automatically tracks modifications
        to persistent entities.

        Args:
            user: Session-managed User with updated attributes.

        Returns:
            The updated User instance.
        """
        self.db.flush()

        return user

    def delete(self, user: User) -> None:
        """
        Mark a user for deletion and flush the session.

        The deletion is not permanent until the
        transaction is committed.

        Args:
            user: User entity to delete.
        """
        self.db.delete(user)
        self.db.flush()
