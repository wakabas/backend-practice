import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from logger.logger_config import LoggerConfig


def get_logger() -> logging.Logger:
    logger = logging.getLogger(LoggerConfig.LOGGER_NAME)

    if logger.hasHandlers():
        return logger

    logger.setLevel(LoggerConfig.LOGS_LEVEL)
    Path(LoggerConfig.LOGGER_DIR_NAME).mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        fmt=LoggerConfig.FORMAT,
        datefmt=LoggerConfig.DATATIME_FORMAT
    )
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(LoggerConfig.LOGS_FILE_NAME,
                                       mode='w',
                                       encoding='utf-8',
                                       maxBytes=LoggerConfig.MAX_BYTES,
                                       backupCount=LoggerConfig.BACKUP_COUNT)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.step = lambda step_num, message: logger.info(f"[STEP {step_num}] {message}")

    return logger
