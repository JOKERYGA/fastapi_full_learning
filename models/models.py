from typing import Any, Dict
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Boolean, ForeignKey, Integer, String, TIMESTAMP, JSON


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True,)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    permissions: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=True)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.now(timezone.utc)
        )
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
