from random import randint

from logger.logger import log
from services.general.models.base_post_grade import Grade
from services.university.models.grade_post_request import GradePostRequest
from services.university.models.grade_statistics_request import GradeStatisticsRequest
from services.university.university_service import UniversityService


class TestGradeStatistics:
    def test_grade_statistics_for_group(self, university_api_session_admin, students_lst, teacher_id, group_id):
        university_service = UniversityService(university_api_session_admin)
        grades = []
        log.step(1, "Set grades to students")
        for student in students_lst:
            grade = randint(Grade.MIN, Grade.MAX)
            university_service.create_grade(GradePostRequest(teacher_id=teacher_id,
                                                             student_id=student,
                                                             grade=grade))
            grades.append(grade)
        log.step(2, "Receive grades statistics")
        received_stats = university_service.get_grades_statistics(GradeStatisticsRequest(group_id=group_id))
        log.step(3, "Perform logic check")
        expected_stats = sum(grades) / len(grades)
        assert expected_stats == received_stats.avg, \
            f"Expected average score - {expected_stats}, but got {received_stats.avg}"
