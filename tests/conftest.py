import pytest
from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.factories.valid_user_factory import ValidUserFactory
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()


@pytest.fixture(scope="session")
def auth_session_service_anonymous() -> ApiSession:
    api_session = ApiSession(url=AuthService.SERVICE_URL)
    return api_session


@pytest.fixture(scope="session")
def university_session_service_anonymous() -> ApiSession:
    api_session = ApiSession(url=UniversityService.SERVICE_URL)
    return api_session


@pytest.fixture(scope="session")
def auth_service_anonymous(auth_session_service_anonymous) -> AuthService:
    auth_service = AuthService(auth_session_service_anonymous)
    return auth_service


@pytest.fixture(scope="function")
def valid_user_creds() -> RegisterRequest:
    return ValidUserFactory.build()


@pytest.fixture(scope="session")
def access_token(auth_service_anonymous: AuthService) -> str:
    valid_user = ValidUserFactory.build()
    auth_service_anonymous.register_user(register_request=valid_user)
    login_response = auth_service_anonymous.login_user(
        LoginRequest(username=valid_user.username,
                     password=valid_user.password))
    return login_response.access_token


@pytest.fixture(scope="session")
def auth_api_session_admin(access_token: str) -> ApiSession:
    api_session = ApiSession(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_session


@pytest.fixture(scope="session")
def university_api_session_admin(access_token: str) -> ApiSession:
    api_session = ApiSession(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_session

@pytest.fixture(scope="function")
def error_collector():
    collector = ErrorCollector()
    yield collector
    collector.verify_all()
