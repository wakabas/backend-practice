import json
import time

import allure
import pytest
import requests
from faker import Faker
from requests import HTTPError

from services.auth.auth_service import AuthService
from services.auth.factories.valid_user_factory import ValidUserFactory
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()


def attach_json(name: str, payload: object) -> None:
    allure.attach(
        json.dumps(payload, ensure_ascii=False, indent=2),
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )


@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 120
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response_auth = requests.get(AuthService.SERVICE_URL + "/docs")
            response_auth.raise_for_status()
            response_university = requests.get(UniversityService.SERVICE_URL + "/docs")
            response_university.raise_for_status()
        except HTTPError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service didn't answer during {timeout} seconds")


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
        LoginRequest(username=valid_user.username, password=valid_user.password)
    )
    return login_response.access_token


@pytest.fixture(scope="session")
def auth_api_session_admin(access_token: str) -> ApiSession:
    api_session = ApiSession(
        url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"}
    )
    return api_session


@pytest.fixture(scope="session")
def university_api_session_admin(access_token: str) -> ApiSession:
    api_session = ApiSession(
        url=UniversityService.SERVICE_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return api_session


@pytest.fixture(scope="session")
def university_service(university_api_session_admin):
    service = UniversityService(university_api_session_admin)
    return service
