"""Скрипт для проверки содержимого БД."""

import sqlite3
from pathlib import Path

# Путь к БД
db_path = Path.home() / "AppData" / "Roaming" / "OGE_Checker" / "oge_checker.db"

print(f"Путь к БД: {db_path}")
print(f"Файл существует: {db_path.exists()}")

if not db_path.exists():
    print("❌ Файл БД не найден!")
    exit(1)

conn = sqlite3.connect(str(db_path))
cur = conn.cursor()

# Список таблиц
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print(f"\nТаблицы в БД: {tables}")

# Структура таблицы users (если есть)
if ("users",) in tables:
    print("\nСтруктура таблицы users:")
    cur.execute("PRAGMA table_info(users)")
    for row in cur.fetchall():
        print(f"  {row}")

conn.close()