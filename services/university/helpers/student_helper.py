import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):

    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def get_student(self, student_id: int) -> requests.Response:
        response = self.api_session.get(f"{self.ROOT_ENDPOINT}{student_id}")
        return response

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_session.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_student(self, student_id: int) -> requests.Response:
        response = self.api_session.delete(f"{self.ROOT_ENDPOINT}{student_id}")
        return response