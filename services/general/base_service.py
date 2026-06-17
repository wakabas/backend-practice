from utils.api_session import ApiSession


class BaseService:

    SERVICE_URL = None

    def __init__(self, api_session: ApiSession):
        self.api_session = api_session