import logging
from logging.handlers import RotatingFileHandler
from .paths import get_logs_dir

_logger: logging.Logger | None = None

def get_logger(name="oge_checker") -> logging.Logger:
    #logging for oge_checker
    global _logger

    if _logger is None:
        _logger = logging.getLogger("oge_checker")
        _logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

        log_file = get_logs_dir() / "oge_checker.log"
        file_handler = RotatingFileHandler(log_file, 
        maxBytes=4*1024*1024,
        backupCount=5,
        encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        _logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        _logger.addHandler(console_handler)

    return logging.getLogger(name)

if __name__ == "__main__":
    log = get_logger()
    log.debug("Это debug — видно только в файле")
    log.info("Это info — видно и в консоли, и в файле")
    log.warning("Это warning")
    log.error("Это error")