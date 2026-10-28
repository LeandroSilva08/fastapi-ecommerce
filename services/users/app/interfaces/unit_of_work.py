"""Define the contract for database transaction management."""

from abc import ABC, abstractmethod


class IUnitOfWork(ABC):
    """
    Define the contract for managing database transactions.

    Ensures that persistence operations can be committed
    or rolled back as a single transactional unit.
    """

    @abstractmethod
    def commit(self) -> None:
        """
        Commit all pending changes in the current transaction.
        """

    @abstractmethod
    def rollback(self) -> None:
        """
        Roll back all uncommitted changes in the transaction.
        """
