"""Скрипт для создания таблиц БД.

"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.oge_checker.db.database import get_engine, get_session, init_db
from src.oge_checker.utils.paths import get_db_path


def main() -> None:
    print("Engine:", get_engine())
    print("DB path:", get_db_path())

    init_db()
    print("Таблицы созданы")

    with get_session() as session:
        print("Session:", session)


if __name__ == "__main__":
    main()