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
    from . import models
    Base.metadata.create_all(bind=_engine)

def get_session() -> Session:
    return SessionLocal()

if __name__ == "__main__":
    print("Engine:", get_engine())
    print("DB path:", get_db_path())
    
    init_db()
    print("init_db() выполнен")
    
    with get_session() as session:
        print("Session:", session)