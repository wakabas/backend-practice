import logging
from pathlib import Path


class LoggerConfig:
    LOGGER_DIR_NAME = "logs"
    LOGGER_NAME = "logger"
    LOGS_FILE_NAME = Path(f"{LOGGER_DIR_NAME}/test.log")
    LOGS_LEVEL = logging.INFO
    FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
    DATATIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
