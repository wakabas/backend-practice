from random import randint

from logger.logger import log
from services.general.models.base_post_grade import Grade
from services.university.factories.grade_factory import GradeFactory
from services.university.models.grade_post_request import GradePostRequest
from services.university.university_service import UniversityService


def grades_lst(num_of_grades: int) -> list[int]:
    grades = [randint(Grade.MIN, Grade.MAX) for _ in range(num_of_grades)]
    return grades


class TestStatistics:
    def test_grade_statistics_for_group(self, university_api_session_admin,
                                        students_lst,
                                        teacher_id,
                                        group_id):
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
        received_stats = university_service.get_grades_statistics(group_id=group_id)
        log.step(3, "Perform logic check, get average score for group")
        expected_stats = sum(grades) / len(grades)
        assert expected_stats == received_stats.avg, \
            f"Expected average score - {expected_stats}, but got {received_stats.avg}"

    def test_grade_statistics_for_student(self, university_api_session_admin, student_id, teacher_id):
        university_service = UniversityService(university_api_session_admin)
        log.step(1, "Generate list of random grades")
        grades = grades_lst(10)
        log.step(2, "Set grades to student")
        for grade in grades:
            university_service.create_grade(GradePostRequest(teacher_id=teacher_id,
                                                             student_id=student_id,
                                                             grade=grade))
        log.step(3, "Perform logic check, get average score for student")
        expected_stats = sum(grades) / len(grades)
        received_stats = university_service.get_grades_statistics(student_id=student_id)
        assert expected_stats == received_stats.avg, \
            f"Expected average score - {expected_stats}, but got {received_stats.avg}"

    def test_grade_statistics_for_teacher(self, university_api_session_admin, teacher_lst, student_id):
        university_service = UniversityService(university_api_session_admin)
        grades_dict = {}
        log.step(1, "Set grades to student by 2 teachers")
        for teacher in teacher_lst:
            grades = university_service.create_multiple_grades(GradeFactory.batch(10,
                                                                                  teacher_id=teacher,
                                                                                  student_id=student_id))
            grades_dict[teacher] = grades
        log.step(2, "Perform Logic check, get average score for each teacher")
        for teacher_id, grades in grades_dict.items():
            grades_values = [grade.grade for grade in grades]
            expected_grades_avg = sum(grades_values) / len(grades)
            received_grades_avg = university_service.get_grades_statistics(teacher_id=teacher_id)
            assert expected_grades_avg == received_grades_avg.avg, \
                f"Expected average score - {expected_grades_avg}, but got {received_grades_avg.avg}"
