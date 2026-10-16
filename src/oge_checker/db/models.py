"""Модели базы данных OGE Checker.
"""

from .database import Base  
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    salt: Mapped[str] = mapped_column(String(64))
    full_name: Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(20), default="teacher")
    school_name: Mapped[str | None]= mapped_column(String(150))
    is_active: Mapped[bool] = mapped_column(default=True)
    last_login: Mapped[datetime | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)