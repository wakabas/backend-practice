import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STATS_ENDPOINT = f"{ROOT_ENDPOINT}stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_session.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grade(self, **kwargs) -> requests.Response:
        response = self.api_session.get(f"{self.ROOT_ENDPOINT}", params=kwargs)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        response = self.api_session.delete(f"{self.ROOT_ENDPOINT}{grade_id}")
        return response

    def get_stats(self, **kwargs) -> requests.Response:
        response = self.api_session.get(f"{self.STATS_ENDPOINT}", params=kwargs)
        return response
