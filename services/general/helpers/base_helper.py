from utils.api_session import ApiSession


class BaseHelper:
    def __init__(self, api_session: ApiSession):
        self.api_session = api_session
