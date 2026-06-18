import random

import pytest
from faker import Faker

from services.general.models.base_post_student import Degree
from services.general.models.base_post_teacher import Subject
from services.university.models.group_delete_request import GroupDeleteRequest
from services.university.models.group_post_request import GroupPostRequest
from services.university.models.student_delete_request import StudentDeleteRequest
from services.university.models.student_post_request import StudentPostRequest
from services.university.models.teacher_delete_request import TeacherDeleteRequest
from services.university.models.teacher_post_request import TeacherPostRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()


@pytest.fixture(scope="function")
def tmp_group_id(university_api_session_admin: ApiSession):
    university_service = UniversityService(university_api_session_admin)
    group = university_service.create_group(group_request=GroupPostRequest(name=faker.word()))
    yield group.id
    university_service.delete_group(GroupDeleteRequest(group_id=group.id))



@pytest.fixture(scope="function")
def tmp_student_id(university_api_session_admin: ApiSession, tmp_group_id):
    university_service = UniversityService(university_api_session_admin)
    student = university_service.create_student(student_request=StudentPostRequest(first_name=faker.first_name(),
                                                                   last_name=faker.last_name(),
                                                                   email=faker.email(),
                                                                   degree=random.choice(list(Degree)),
                                                                   phone=faker.numerify("+7##########"),
                                                                   group_id=tmp_group_id))
    yield student.id
    university_service.delete_student(StudentDeleteRequest(student_id=student.id))


@pytest.fixture(scope="function")
def tmp_teacher_id(university_api_session_admin: ApiSession):
    university_service = UniversityService(university_api_session_admin)
    teacher = university_service.create_teacher(teacher_request=TeacherPostRequest(first_name=faker.first_name(),
                                                                   last_name=faker.last_name(),
                                                                   subject=random.choice(list(Subject)),
                                                                   ))
    yield teacher.id
    university_service.delete_teacher(TeacherDeleteRequest(teacher_id=teacher.id))
