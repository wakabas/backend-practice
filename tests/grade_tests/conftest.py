from random import randint
from typing import Any

import pytest
from faker import Faker

from services.general.models.base_post_grade import Grade
from services.university.factories.grade_factory import GradeFactory
from services.university.factories.student_factory import StudentFactory
from services.university.factories.teacher_factory import TeacherFactory
from services.university.models.grade_post_request import GradePostRequest
from services.university.models.group_post_request import GroupPostRequest

faker = Faker()


@pytest.fixture(scope="function")
def group_id(university_service) -> int:
    group = university_service.create_group(
        group_request=GroupPostRequest(name=faker.word())
    )
    return group.id


@pytest.fixture(scope="function")
def grades_lst(num_of_grades: int) -> list[int]:
    grades = [randint(Grade.MIN, Grade.MAX) for _ in range(num_of_grades)]
    return grades


@pytest.fixture(scope="function")
def student_id(university_service, group_id: int) -> int:
    student = university_service.create_student(
        student_request=StudentFactory.build(group_id=group_id)
    )
    return student.id


@pytest.fixture(scope="function")
def teacher_id(university_service) -> int:
    teacher = university_service.create_teacher(teacher_request=TeacherFactory.build())
    return teacher.id


@pytest.fixture(scope="function")
def students_lst(university_service, group_id) -> list[int]:
    students_requests = StudentFactory.batch(10, group_id=group_id)
    student_ids = [
        student.id
        for student in university_service.create_multiple_students(students_requests)
    ]
    return student_ids


@pytest.fixture(scope="function", params=[1, 2], ids=["teacher_1", "teacher_2"])
def teacher_and_grades(request, university_service, teacher_id, group_id, student_id) -> tuple[int, list[Any]]:

    grades = university_service.create_multiple_grades(
        GradeFactory.batch(10, teacher_id=teacher_id, student_id=student_id)
    )
    grades_values = [grade.grade for grade in grades]
    return teacher_id, grades_values


@pytest.fixture(scope="function")
def student_group_with_marks(university_service, grades_lst, teacher_id, students_lst):
    for student, grade in zip(students_lst, grades_lst):
        university_service.create_grade(
            GradePostRequest(teacher_id=teacher_id, student_id=student, grade=grade)
        )
    return students_lst[0].group_id

@pytest.fixture(scope="function")
def student_with_grades(university_service, grades_lst, teacher_id, student_id):
    for grade in grades_lst:
        university_service.create_grade(
            GradePostRequest(
                teacher_id=teacher_id, student_id=student_id, grade=grade
            )
        )
    return student_id