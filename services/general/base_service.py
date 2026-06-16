from utils.api_session import ApiSession


class BaseService:

    SERVICE_URL = None

    def __init__(self, session: ApiSession):
        self.session = session