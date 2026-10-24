"""Тест аутентификации."""
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.oge_checker.core.auth import AuthError, AuthService
from src.oge_checker.db.database import get_session, init_db
from src.oge_checker.db.models import User


def main() -> None:
    init_db()
    session = get_session()
    auth = AuthService(session)

    # Очистка
    session.query(User).delete()
    session.commit()

    # 1. Регистрация
    print("=== Регистрация ===")
    user = auth.register("admin", "admin123", "Администратор", role="admin")
    print(f"✅ Создан: {user.username} ({user.full_name})")
    print(f"   Хеш: {user.password_hash[:20]}...")

    # 2. Попытка регистрации с тем же username
    print("\n=== Повторная регистрация ===")
    try:
        auth.register("admin", "other123", "Другой")
        print("❌ Должно было упасть!")
    except AuthError as e:
        print(f"✅ Ошибка: {e}")

    # 3. Вход с правильным паролем
    print("\n=== Вход (правильный пароль) ===")
    logged = auth.login("admin", "admin123")
    print(f"✅ Вход успешен: {logged.full_name}")
    print(f"   last_login: {logged.last_login}")

    # 4. Вход с неправильным паролем
    print("\n=== Вход (неправильный пароль) ===")
    try:
        auth.login("admin", "wrong")
        print("❌ Должно было упасть!")
    except AuthError as e:
        print(f"✅ Ошибка: {e}")

    # 5. Смена пароля
    print("\n=== Смена пароля ===")
    auth.change_password(user, "admin123", "newpass456")
    print("✅ Пароль изменён")

    # 6. Вход со старым паролем
    print("\n=== Вход (старый пароль) ===")
    try:
        auth.login("admin", "admin123")
        print("❌ Должно было упасть!")
    except AuthError as e:
        print(f"✅ Ошибка: {e}")

    # 7. Вход с новым паролем
    print("\n=== Вход (новый пароль) ===")
    logged = auth.login("admin", "newpass456")
    print(f"✅ Вход успешен: {logged.full_name}")

    session.close()


if __name__ == "__main__":
    main()