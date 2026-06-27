from random import randint

from logger.logger import log
from services.general.models.base_post_grade import Grade
from services.university.models.grade_post_request import GradePostRequest


class TestGrade:
    def test_grade_create(self,
                          university_service,
                          teacher_id,
                          student_id):
        log.step(1, "Create grade")
        grade_response = university_service.create_grade(GradePostRequest(teacher_id=teacher_id,
                                                                          student_id=student_id,
                                                                          grade=randint(Grade.MIN, Grade.MAX)))
        log.step(2, "Verification for grade ids (teacher_id, student_id)")
        assert grade_response.teacher_id == teacher_id and grade_response.student_id == student_id, (
            f"Expected id for teacher or student: teacher_id - {teacher_id}, student_id - {student_id}\n"
            f"Actual ids: teacher - {grade_response.teacher_id}, student - {grade_response.student_id}")
