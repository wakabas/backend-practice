import logging
from pathlib import Path


class LoggerConfig:
    LOGGER_DIR_NAME = "logs"
    LOGGER_NAME = "logger"
    LOGS_FILE_NAME = Path(f"{LOGGER_DIR_NAME}/test.log")
    LOGS_LEVEL = logging.INFO
    FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
    DATATIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
    MAX_BYTES = 1024 * 1024 * 10
    BACKUP_COUNT = 3
