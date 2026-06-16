import pytest
from faker import Faker

from services.auth.auth_service import AuthService
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()

@pytest.fixture(scope="session")
def auth_session_service_anonymous():
    session = ApiSession(url=AuthService.SERVICE_URL)
    return session

@pytest.fixture(scope="session")
def university_session_service_anonymous():
    session = ApiSession(url=UniversityService.SERVICE_URL)
    return session

