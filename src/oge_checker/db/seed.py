"""Начальное заполнение БД."""

from sqlalchemy.orm import Session

from ..core.auth import AuthService
from .models import Scale, User

SCALES_2026 = {
    "Русский язык":   {"max_score": 33, "grade2_max": 14, "grade3_max": 21, "grade4_max": 28},
    "Математика":     {"max_score": 31, "grade2_max": 7,  "grade3_max": 14, "grade4_max": 22},
    "Физика":         {"max_score": 45, "grade2_max": 9,  "grade3_max": 18, "grade4_max": 29},
    "Химия":          {"max_score": 40, "grade2_max": 9,  "grade3_max": 18, "grade4_max": 28},
    "Биология":       {"max_score": 45, "grade2_max": 12, "grade3_max": 23, "grade4_max": 34},
    "История":        {"max_score": 37, "grade2_max": 9,  "grade3_max": 18, "grade4_max": 27},
    "Обществознание": {"max_score": 37, "grade2_max": 11, "grade3_max": 20, "grade4_max": 29},
    "Информатика":    {"max_score": 19, "grade2_max": 4,  "grade3_max": 9,  "grade4_max": 14},
    "География":      {"max_score": 31, "grade2_max": 9,  "grade3_max": 16, "grade4_max": 23},
    "Английский":     {"max_score": 68, "grade2_max": 28, "grade3_max": 44, "grade4_max": 57},
    "Литература":     {"max_score": 42, "grade2_max": 14, "grade3_max": 24, "grade4_max": 33},
}

def seed_default_admin(session) -> User | None:
    count = session.query(User).count()
    if count > 0:
        return None
    else:
        auth = AuthService(session)
        admin = auth.register("admin", "admin123", "Администратор", role="admin")
        return admin

def seed_scales(session):
    created_scales = 0
    for subj, data in SCALES_2026.items():
        exists = session.query(Scale).filter_by(subject=subj, year=2026).first() 
        if exists is None:
            scale = Scale(subject=subj, year=2026, **data)
            session.add(scale)
            created_scales += 1
        session.commit()
    return created_scales
    
def seed_all(session: Session) -> None:
    admin = seed_default_admin(session)
    if admin:
        print(f"Создан админ: {admin.username}")
    
    count = seed_scales(session)
    if count > 0:
        print(f"Создано шкал: {count}")
    else:
        print("Шкалы уже есть")