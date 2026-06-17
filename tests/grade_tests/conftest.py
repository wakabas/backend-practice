import random

from faker import Faker
import pytest

from services.general.models.base_post_student import Degree
from services.university.models.group_post_request import GroupPostRequest
from services.university.models.student_post_request import StudentPostRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession


faker = Faker()


@pytest.fixture(scope="session")
def tmp_group_id(university_api_session_admin: ApiSession):
    university_service = UniversityService(university_api_session_admin)
    group = university_service.create_group(GroupPostRequest(name=faker.word()))
    return group.id

@pytest.fixture(scope="session")
def tmp_student(university_api_session_admin: ApiSession, tmp_group_id):
    university_service = UniversityService(university_api_session_admin)
    university_service.create_student(StudentPostRequest(first_name=faker.first_name(),
                                                         last_name=faker.last_name(),
                                                         email=faker.email(),
                                                         degree=random.choice(Degree),
                                                         phone=faker.numerify("+7##########"),
                                                         group_id=tmp_group_id))