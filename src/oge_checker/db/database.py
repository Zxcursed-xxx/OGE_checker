from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from ..utils.paths import get_db_path

class Base(DeclarativeBase):
    pass

_engine = create_engine(f"sqlite:///{get_db_path()}",
    echo=True,
    connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, expire_on_commit=False)

def get_engine():
    return _engine

def init_db() -> None:
    """Создать все таблицы, если их нет."""
    from . import models  # noqa: F401
    Base.metadata.create_all(bind=_engine)

def get_session() -> Session:
    return SessionLocal()

