# 📊 OGE Checker

![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt-6-41CD52?logo=qt&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-in%20development-orange)

**Автоматизированное рабочее место учителя для подсчёта результатов ОГЭ.**

Приложение помогает учителям быстро вводить баллы учеников, автоматически
переводить их в оценки по актуальным шкалам и генерировать подробные отчёты
по классу.

---

## ✨ Возможности

- 🔐 **Многопользовательский режим** — роли «учитель» и «администратор»
- 📝 **Быстрый ввод баллов** — таблица, горячие клавиши, автосохранение
- ⚖️ **Гибкие шкалы перевода** — редактируются под текущий год
- 📊 **Автоматические отчёты** — сводка, распределение оценок, сложные задания
- 📤 **Экспорт в Excel и PDF**
- 💾 **Локальная БД SQLite** — работает без интернета
- 🔄 **Резервное копирование** базы данных
- 🌙 **Светлая и тёмная темы**

---

## 🖼 Скриншоты

> Скриншоты появятся после реализации интерфейса. Следите за обновлениями!

<!--
| Вход | Дашборд | Ввод баллов |
|------|---------|-------------|
| ![login](docs/screenshots/login.png) | ![dashboard](docs/screenshots/dashboard.png) | ![entry](docs/screenshots/data_entry.png) |
-->

---

## 🚀 Быстрый старт

### Требования

- **Python** 3.11 или выше
- **Windows** / **Linux** / **macOS**

### Установка

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Zxcursed-xxx/OGE_checker.git
cd OGE_checker

# 2. Создать виртуальное окружение
python -m venv venv

# 3. Активировать его
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

# 4. Установить зависимости
pip install -r requirements.txt
```

### Запуск

```bash
python -m src.oge_checker.main
```

> ⚠️ Приложение находится в активной разработке. Функционал может меняться.

При первом запуске создаётся администратор по умолчанию:

- **Логин:** `admin`
- **Пароль:** `admin123` — обязательно смените после первого входа!

---

## 📁 Структура проекта

```
OGE_checker/
├── src/
│   └── oge_checker/
│       ├── core/         # Бизнес-логика (подсчёт, шкалы, отчёты)
│       ├── db/           # Работа с SQLite (модели, миграции)
│       ├── ui/           # Интерфейс PyQt6
│       └── utils/        # Утилиты (пути, бэкапы, экспорт)
├── tests/                # Тесты (pytest)
├── docs/                 # Документация и скриншоты
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Технологии

| Слой | Технология |
|------|------------|
| Язык | Python 3.11+ |
| GUI | PyQt6 / PySide6 |
| БД | SQLite 3 + SQLAlchemy 2.0 |
| Хеширование | bcrypt |
| Графики | Matplotlib |
| Экспорт | openpyxl, reportlab |
| Сборка | PyInstaller |
| Тесты | pytest |

---

## 🗺 Roadmap

- [x] Создание репозитория и документации
- [ ] Спринт 1 — Фундамент: БД, аутентификация, экран входа
- [ ] Спринт 2 — Основной функционал: классы, шкалы, ввод баллов
- [ ] Спринт 3 — Отчёты и экспорт в Excel/PDF
- [ ] Спринт 4 — Админ-панель
- [ ] Спринт 5 — Полировка UI, тёмная тема
- [ ] Спринт 6 — Сборка .exe, релиз v1.0

---

## 🤝 Вклад в проект

Проект открыт для идей и pull request'ов. Если хочешь что-то улучшить —
сначала открой **Issue** с описанием предложения.

```bash
git checkout -b feature/название-фичи
git commit -m "feat: краткое описание"
git push origin feature/название-фичи
```

---

## 📄 Лицензия

Распространяется под лицензией **MIT** — см. файл [LICENSE](LICENSE).

---

## 👨‍💻 Автор

**Zxcursed-xxx** — [github.com/Zxcursed-xxx](https://github.com/Zxcursed-xxx)

Проект создан в помощь учителям, чтобы рутина с подсчётом баллов
занимала минуты, а не часы. ❤️
