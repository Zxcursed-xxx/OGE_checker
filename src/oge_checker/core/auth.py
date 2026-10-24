"""Аутентификация пользователей."""

from datetime import datetime, timezone

import bcrypt
from sqlalchemy.orm import Session

from ..db.models import User


class AuthError(Exception):
    """Ошибка аутентификации."""
    pass


class AuthService:
    """Сервис аутентификации."""

    def __init__(self, session: Session):
        self.session = session

    def hash_password(self, password: str) -> str:
        """Захешировать пароль через bcrypt"""
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt).decode("utf-8")

    def verify_password(self, password: str, password_hash: str) -> bool:
        """Проверить пароль против хеша"""
        password_bytes = password.encode("utf-8")
        hash_bytes = password_hash.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hash_bytes)

    def register(self, username: str, password: str, full_name: str, role: str = "teacher") -> User:
        """Зарегистрировать нового пользователя"""
        exist = self.session.query(User).filter_by(username=username).first()

        if exist is not None:
            raise AuthError(f"Пользователь '{username}' уже существует")

        user = User(username=username, password_hash=self.hash_password(password), salt="", full_name=full_name, role=role)
        self.session.add(user)
        self.session.commit()
        return user

    def login(self, username: str, password: str) -> User:
        user = self.session.query(User).filter_by(username=username).first()
        if user is None:
            raise AuthError("Неверный логин или пароль")

        if not user.is_active:
            raise AuthError("Аккаунт заблокирован")

        if not self.verify_password(password, user.password_hash):
            raise AuthError("Неверный логин или пароль")

        user.last_login = datetime.now(timezone.utc)
        self.session.commit()
        return user

    def change_password(self, user: User, old_password: str, new_password: str,) -> None:
        if not self.verify_password(old_password, user.password_hash):
            raise AuthError("Неверный старый пароль")

        user.password_hash = self.hash_password(new_password)
        self.session.commit()