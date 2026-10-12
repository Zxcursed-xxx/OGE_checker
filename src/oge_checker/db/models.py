"""Модели базы данных OGE Checker.

Здесь будут описаны таблицы: User, Class, Student, Scale, Check, Result.
"""

from .database import Base  # noqa: F401

# Пока моделей нет — файл пустой, чтобы init_db() не падал.
# На следующем шаге добавим сюда User.