"""Скрипт проверки содержимого БД.

"""

import sqlite3
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.oge_checker.utils.paths import get_db_path


def main() -> None:
    db_path = get_db_path()
    print(f"Путь к БД: {db_path}")
    print(f"Файл существует: {db_path.exists()}")

    if not db_path.exists():
        print("❌ Файл БД не найден!")
        return

    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    print(f"\nТаблицы в БД: {tables}")

    for table_name, in tables:
        print(f"\nСтруктура таблицы {table_name}:")
        cur.execute(f"PRAGMA table_info({table_name})")
        for row in cur.fetchall():
            print(f"  {row}")

    conn.close()


if __name__ == "__main__":
    main()