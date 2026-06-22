import pytest
from faker import Faker

from services.university.factories.student_factory import StudentFactory
from services.university.factories.teacher_factory import TeacherFactory
from services.university.models.group_post_request import GroupPostRequest
from services.university.university_service import UniversityService
from utils.api_session import ApiSession

faker = Faker()


@pytest.fixture(scope="module")
def group_id(university_api_session_admin: ApiSession) -> int:
    university_service = UniversityService(university_api_session_admin)
    group = university_service.create_group(group_request=GroupPostRequest(name=faker.word()))
    return group.id


@pytest.fixture(scope="function")
def student_id(university_api_session_admin: ApiSession, group_id: int) -> int:
    university_service = UniversityService(university_api_session_admin)
    student = university_service.create_student(student_request=StudentFactory.build(group_id=group_id))
    return student.id


@pytest.fixture(scope="function")
def teacher_id(university_api_session_admin: ApiSession) -> int:
    university_service = UniversityService(university_api_session_admin)
    teacher = university_service.create_teacher(teacher_request=TeacherFactory.build())
    return teacher.id


@pytest.fixture(scope="function")
def students_lst(university_api_session_admin: ApiSession, group_id) -> list[int]:
    university_service = UniversityService(university_api_session_admin)
    students_requests = StudentFactory.batch(10, group_id=group_id)
    student_ids = [student.id for student in university_service.create_multiple_students(students_requests)]
    return student_ids


@pytest.fixture(scope="function")
def teacher_lst(university_api_session_admin: ApiSession) -> list[int]:
    university_service = UniversityService(university_api_session_admin)
    teacher_requests = TeacherFactory.batch(2)
    teacher_ids = [teacher.id for teacher in university_service.create_multiple_teachers(teacher_requests)]
    return teacher_ids
