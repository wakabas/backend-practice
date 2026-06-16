import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):

    ENDPOINT_PREFIX = "/groups"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def get_group(self, group_id: int) -> requests.Response:
        response = self.api_session.get(f"{self.ROOT_ENDPOINT}{group_id}")
        return response

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_session.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_group(self, group_id: int) -> requests.Response:
        response = self.api_session.delete(f"{self.ROOT_ENDPOINT}{group_id}")
        return response