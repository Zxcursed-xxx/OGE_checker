"""Запуск seed БД.

Запуск: py scripts/seed.py
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.oge_checker.db.database import get_session, init_db
from src.oge_checker.db.seed import seed_all


def main() -> None:
    init_db()
    session = get_session()
    
    print("=== Seed БД ===")
    seed_all(session)
    
    session.close()
    print("=== Готово ===")


if __name__ == "__main__":
    main()