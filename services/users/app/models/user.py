from datetime import datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    Identity,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        # If an address is provided, require its main fields
        CheckConstraint(
            """
            (street IS NULL AND city IS NULL
             AND postal_code IS NULL AND country IS NULL)
            OR
            (street IS NOT NULL AND city IS NOT NULL
             AND postal_code IS NOT NULL AND country IS NOT NULL)
            """,
            name="ck_users_address_complete",
        ),
    )

    id: Mapped[int] = mapped_column(
        Identity(),
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    street: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    postal_code: Mapped[str | None] = mapped_column(
        String(20),
        CheckConstraint(
            "postal_code ~ '^[A-Za-z0-9][A-Za-z0-9 -]*$'",
            name="ck_users_postal_code_format",
        ),
        nullable=True,
    )

    country: Mapped[str | None] = mapped_column(
        String(2),
        CheckConstraint(
            "country ~ '^[A-Z]{2}$'",
            name="ck_users_country_format",
        ),
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        CheckConstraint(
            "email ~* '^[^[:space:]@]+@[^[:space:]@]+\\.[^[:space:]@]+$'",
            name="ck_users_email_format",
        ),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        server_default="true",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
