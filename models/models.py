from datetime import datetime, timezone
from typing import Any, Dict, List
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP, JSON


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = "roles"
    
    id: Mapped[int] = mapped_column(primary_key=True,)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    permissions: Mapped[Dict[str, Any]] = mapped_column(JSON)


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now(timezone.utc))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'))