"""Модели базы данных OGE Checker.
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    """Пользователь: администратор или учитель"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    salt: Mapped[str] = mapped_column(String(64))
    full_name: Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(20), default="teacher")
    school_name: Mapped[str | None] = mapped_column(String(150))
    is_active: Mapped[bool] = mapped_column(default=True)
    last_login: Mapped[datetime | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    classes: Mapped[list["Class"]] = relationship(back_populates="teacher")

class Class(Base):
    """Класс (9А)"""
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    year: Mapped[int] = mapped_column(default=2026)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    teacher: Mapped["User"] = relationship(back_populates="classes")

    students: Mapped[list["Student"]] = relationship(back_populates="class_")

class Student(Base):
    """Ученик"""
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))

    class_: Mapped["Class"] = relationship(back_populates="students")

class Scale(Base):
    """Оценки и баллы"""
    __tablename__ = "scales"
    __table_args__ = (
        UniqueConstraint("subject", "year", name="uq_scales_subject_year"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(default=2026)
    max_score: Mapped[int]
    grade2_max: Mapped[int]
    grade3_max: Mapped[int]
    grade4_max: Mapped[int]

