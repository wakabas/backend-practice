import json
from functools import wraps

import requests
from requests import HTTPError

from logger.logger import log
from utils.api_session import ApiSession
from utils.json_utils import JsonUtils


def log_error_status(func):
    @wraps(func)
    def _log_error_status(*args, **kwargs):
        response: requests.Response = func(*args, **kwargs)
        body = json.dumps(response.json(), indent=4) if JsonUtils.is_json(response.text) else response.text
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            log.error(f"Error within method: {func.__name__}\n"
                      f"Response status code: {response.status_code}\n"
                      f"{body}\n"
                      f"Details: {http_err}\n")
            raise
        return response

    return _log_error_status


class BaseHelper:

    def __init__(self, api_session: ApiSession):
        self.api_session = api_session
