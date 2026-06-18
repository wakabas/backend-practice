from collections import namedtuple
from random import randint

import pytest
from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()


@pytest.fixture(scope="session")
def auth_session_service_anonymous():
    api_session = ApiSession(url=AuthService.SERVICE_URL)
    return api_session


@pytest.fixture(scope="session")
def university_session_service_anonymous():
    api_session = ApiSession(url=UniversityService.SERVICE_URL)
    return api_session


@pytest.fixture(scope="session")
def auth_service_anonymous(auth_session_service_anonymous):
    auth_service = AuthService(auth_session_service_anonymous)
    return auth_service


@pytest.fixture(scope="session")
def valid_user_creds():
    valid_user = namedtuple("user", ["username", "password"])
    username = faker.user_name()
    password = faker.password(length=10,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    return valid_user(username=username, password=password)


@pytest.fixture(scope="session")
def access_token(auth_service_anonymous, valid_user_creds):
    auth_service_anonymous.register_user(register_request=RegisterRequest(username=valid_user_creds.username,
                                                                          password=valid_user_creds.password,
                                                                          password_repeat=valid_user_creds.password,
                                                                          email=faker.email()))
    login_response = auth_service_anonymous.login_user(
        LoginRequest(username=valid_user_creds.username,
                     password=valid_user_creds.password))
    return login_response.access_token


@pytest.fixture(scope="session")
def auth_api_session_admin(access_token):
    api_session = ApiSession(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_session


@pytest.fixture(scope="session")
def university_api_session_admin(access_token):
    api_session = ApiSession(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_session
