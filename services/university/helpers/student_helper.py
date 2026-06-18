import requests

from services.general.helpers.base_helper import BaseHelper, log_error_status


class StudentHelper(BaseHelper):

    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    @log_error_status
    def get_student(self, student_id: int) -> requests.Response:
        response = self.api_session.get(f"{self.ROOT_ENDPOINT}{student_id}")
        return response

    @log_error_status
    def post_student(self, json: dict) -> requests.Response:
        response = self.api_session.post(self.ROOT_ENDPOINT, json=json)
        return response

    @log_error_status
    def delete_student(self, student_id: int) -> requests.Response:
        response = self.api_session.delete(f"{self.ROOT_ENDPOINT}{student_id}")
        return response