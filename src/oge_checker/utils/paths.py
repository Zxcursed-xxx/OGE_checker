from pathlib import Path
import platform
import os

APP_NAME = "OGE_Checker"

def get_app_data_dir() -> Path:
    # return path to dir

    system = platform.system()

    if system == "Windows":
        p = os.environ.get("APPDATA") 
        app_dir = Path(p) / APP_NAME
    elif system == "Darwin":
        app_dir = Path.home() / "Library" / "Application Support" / APP_NAME
    else:
        p = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local" / "share")
        app_dir = Path(p) / APP_NAME

    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir


def get_db_path() -> Path:
    #return path to db
    return get_app_data_dir() / "oge_checker.db"

def get_logs_dir() -> Path:
    #returns path to logs
    logs = get_app_data_dir() / "logs"
    logs.mkdir(exist_ok=True)
    return logs

def get_backups_dir() -> Path:
    #returns path to backups
    backups = get_app_data_dir() / "backups"
    backups.mkdir(exist_ok=True)
    return backups

