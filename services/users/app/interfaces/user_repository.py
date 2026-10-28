"""Define the contract for user repository operations."""

from abc import ABC, abstractmethod

from app.models.user import User


class IUserRepository(ABC):
    """
    Abstract contract for user persistence operations.

    Defines the operations required to retrieve, create,
    update, and delete users independently of the
    underlying persistence implementation.
    """

    @abstractmethod
    def get_all(self) -> list[User]:
        """
        Retrieve all users.

        Returns:
            A list of User instances, or an empty list
            if no users exist.
        """

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by their unique identifier.

        Args:
            user_id: Unique identifier of the user.

        Returns:
            The matching User instance, or None if not found.
        """

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by their email address.

        Args:
            email: Email address to search for.

        Returns:
            The matching User instance, or None if not found.
        """

    @abstractmethod
    def create(self, user: User) -> User:
        """
        Add a new user to the persistence context.

        The operation must not commit the transaction.

        Args:
            user: User entity to create.

        Returns:
            The User instance after persistence operations.
        """

    @abstractmethod
    def update(self, user: User) -> User:
        """
        Persist changes to an existing user.

        The user must be managed by the current session.
        The operation must not commit the transaction.

        Args:
            user: User entity with updated attributes.

        Returns:
            The updated User instance.
        """

    @abstractmethod
    def delete(self, user: User) -> None:
        """
        Delete an existing user.

        The operation must not commit the transaction.

        Args:
            user: User entity to delete.
        """
