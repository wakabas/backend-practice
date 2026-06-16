import json
import logging
from functools import wraps

import curlify
import requests

from logger.logger_config import LoggerConfig
from utils.json_utils import JsonUtils

logger = logging.getLogger(LoggerConfig.LOGGER_NAME)


def log_response(func):
    @wraps(func)
    def _log_response(*args, **kwargs) -> requests.Response:
        try:
            response = func(*args, **kwargs)
            logger.info(f"Request: {curlify.to_curl(response).request}")
            body = json.dumps(response.json(), indent=4) if JsonUtils.is_json(response.text) else response.text
            logger.info(f"Response status code = '{response.status_code}', "
                        f"elapsed_time = '{response.elapsed.total_seconds()}'\n{body}\n")
            return response
        except Exception as e:
            logger.error(f"Error within method {func.__name__}: {e}")
            raise e
    return _log_response

class ApiSession:

    def __init__(self, url: str, headers: dict = None):
        if headers is None:
            headers = {}
        self.url = url
        self.session = requests.Session()
        self.session.headers.update(headers)

    @log_response
    def get(self, endpoint_url: str, **kwargs) -> requests.Response:
        response = self.session.get(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def post(self, endpoint_url: str, data=None, json=None, **kwargs) -> requests.Response:
        response = self.session.post(self.url + endpoint_url, data, json, **kwargs)
        return response

    @log_response
    def delete(self, endpoint_url: str, **kwargs) -> requests.Response:
        response = self.session.delete(self.url + endpoint_url, **kwargs)
        return response