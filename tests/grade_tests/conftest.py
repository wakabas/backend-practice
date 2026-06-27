import pytest
from faker import Faker

from services.university.factories.student_factory import StudentFactory
from services.university.factories.teacher_factory import TeacherFactory
from services.university.models.group_post_request import GroupPostRequest

faker = Faker()


@pytest.fixture(scope="function")
def group_id(university_service) -> int:
    group = university_service.create_group(group_request=GroupPostRequest(name=faker.word()))
    return group.id


@pytest.fixture(scope="function")
def student_id(university_service, group_id: int) -> int:
    student = university_service.create_student(student_request=StudentFactory.build(group_id=group_id))
    return student.id


@pytest.fixture(scope="function")
def teacher_id(university_service) -> int:
    teacher = university_service.create_teacher(teacher_request=TeacherFactory.build())
    return teacher.id


@pytest.fixture(scope="function")
def students_lst(university_service, group_id) -> list[int]:
    students_requests = StudentFactory.batch(10, group_id=group_id)
    student_ids = [student.id for student in university_service.create_multiple_students(students_requests)]
    return student_ids


@pytest.fixture(scope="function", params=[1, 2], ids=["teacher_1", "teacher_2"])
def single_teacher(request, university_service, teacher_id) -> int:
    return teacher_id
