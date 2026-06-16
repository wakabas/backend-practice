import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):

    ENDPOINT_PREFIX = "/teachers"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def get_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_session.get(f"{self.ROOT_ENDPOINT}{teacher_id}")
        return response

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_session.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_session.delete(f"{self.ROOT_ENDPOINT}{teacher_id}")
        return response