import requests

from services.general.helpers.base_helper import BaseHelper, log_error_status


class AuthenticationHelper(BaseHelper):
    ENDPOINT_PREFIX = "/auth"
    REGISTER_ENDPOINT = f"{ENDPOINT_PREFIX}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT_PREFIX}/login/"

    @log_error_status
    def post_register(self, data: dict) -> requests.Response:
        response = self.api_session.post(self.REGISTER_ENDPOINT, data=data)
        return response

    @log_error_status
    def post_login(self, data: dict) -> requests.Response:
        response = self.api_session.post(self.LOGIN_ENDPOINT, data=data)
        return response
