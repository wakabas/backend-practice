from random import randint

from logger.logger import log
from services.general.models.base_post_grade import Grade
from services.university.factories.grade_factory import GradeFactory
from services.university.factories.student_factory import StudentFactory
from services.university.models.grade_post_request import GradePostRequest
from services.university.university_service import UniversityService
from utils.error_collector import ErrorCollector


def grades_lst(num_of_grades: int) -> list[int]:
    grades = [randint(Grade.MIN, Grade.MAX) for _ in range(num_of_grades)]
    return grades

collector = ErrorCollector()

class TestStatistics:
    def test_grade_statistics_for_group(self,
                                        university_api_session_admin,
                                        students_lst,
                                        teacher_id,
                                        group_id):
        university_service = UniversityService(university_api_session_admin)
        grades = grades_lst(num_of_grades=10)
        log.step(1, "Set grades to students in the same group")
        for student, grade in zip(students_lst, grades):
            university_service.create_grade(GradePostRequest(teacher_id=teacher_id,
                                                             student_id=student,
                                                             grade=grade))
        received_stats = university_service.get_grades_statistics(group_id=group_id)
        log.step(2, "Checking count of grades for group")
        expected_count = len(grades)
        collector.check(expected_count == received_stats.count,
                        f"Expected count - {expected_count}, but got {received_stats.count}")
        log.step(3, "Perform logic check, get average score for group")
        expected_stats = sum(grades) / len(grades)
        collector.check(expected_stats == received_stats.avg,
                        f"Expected average score - {expected_stats}, but got {received_stats.avg}")
        collector.verify_all_errors()

    def test_grade_statistics_for_student(self,
                                          university_api_session_admin,
                                          student_id,
                                          teacher_id):
        university_service = UniversityService(university_api_session_admin)
        log.step(1, "Generate list of random grades")
        grades = grades_lst(num_of_grades=10)
        log.step(2, "Set grades to student")
        for grade in grades:
            university_service.create_grade(GradePostRequest(teacher_id=teacher_id,
                                                             student_id=student_id,
                                                             grade=grade))
        received_stats = university_service.get_grades_statistics(student_id=student_id)
        log.step(3, "Checking count of grades")
        expected_count = len(grades)
        collector.check(expected_count == received_stats.count,
                        f"Expected count - {expected_count}, but got {received_stats.count}")
        log.step(4, "Perform logic check, get average score for student")
        expected_stats = sum(grades) / len(grades)
        collector.check(expected_stats == received_stats.avg,
                        f"Expected average score - {expected_stats}, but got {received_stats.avg}")
        collector.verify_all_errors()

    def test_grade_statistics_for_teacher(self,
                                          university_api_session_admin,
                                          group_id,
                                          single_teacher):
        university_service = UniversityService(university_api_session_admin)
        log.step(1, "Set grades to student by 2 teachers")
        student = university_service.create_student(student_request=StudentFactory.build(group_id=group_id))
        grades = university_service.create_multiple_grades(GradeFactory.batch(10,
                                                                              teacher_id=single_teacher,
                                                                              student_id=student.id))
        grades_values = [grade.grade for grade in grades]
        received_grades_stat = university_service.get_grades_statistics(teacher_id=single_teacher)
        log.step(2, "Check count of grades given by each teacher")
        expected_count = len(grades_values)
        collector.check(expected_count == received_grades_stat.count,
                        f"Expected count - {expected_count}, but got {received_grades_stat.count}")
        log.step(3, "Perform logic check, get average score for each teacher")
        expected_grades_avg = sum(grades_values) / expected_count
        collector.check(expected_grades_avg == received_grades_stat.avg,
                        f"Expected average score - {expected_grades_avg}, but got {received_grades_stat.avg}")
        collector.verify_all_errors()
