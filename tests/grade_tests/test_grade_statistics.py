import allure

from logger.logger import log
from utils.error_collector import ErrorCollector

collector = ErrorCollector()


@allure.suite("Tests for grade statistics, count")
class TestGradeCount:
    @allure.title("Test grade count for group")
    def test_grade_count_for_group(
        self, university_service, grades_lst, student_group_with_marks
    ):
        with allure.step("Step 1: Receive grades statistics for group"):
            log.step(1, "Receive grades statistics for group")
            received_stats = university_service.get_grades_statistics(
                group_id=student_group_with_marks
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for group"
        ):
            log.step(
                2,
                "Perform logic check, compare actual and received count of grades for group",
            )
            expected_count = len(grades_lst)
            collector.check(
                expected_count == received_stats.count,
                f"Expected count - {expected_count}, but got {received_stats.count}",
            )
        collector.verify_all_errors()

    @allure.title("Test grade count for student")
    def test_grade_count_for_student(
        self, university_service, student_with_grades, grades_lst
    ):
        with allure.step("Step 1: Receive grades statistics for student"):
            log.step(1, "Receive grades statistics for student")
            received_stats = university_service.get_grades_statistics(
                student_id=student_with_grades
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for student"
        ):
            log.step(
                2,
                "Perform logic check, compare actual and received count of grades for student",
            )
            expected_count = len(grades_lst)
            collector.check(
                expected_count == received_stats.count,
                f"Expected count - {expected_count}, but got {received_stats.count}",
            )
        collector.verify_all_errors()

    @allure.title("Test grade count for teacher")
    def test_grade_count_for_teacher(self, university_service, teacher_and_grades):
        single_teacher, grades_values = teacher_and_grades
        with allure.step("Step 1: Receive grades statistics for teacher"):
            log.step(1, "Receive grades statistics for teacher")
            received_grades_stat = university_service.get_grades_statistics(
                teacher_id=single_teacher
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for teacher"
        ):
            log.step(
                2, "Perform logic check, compare actual and received count of grades"
            )
            expected_count = len(grades_values)
            collector.check(
                expected_count == received_grades_stat.count,
                f"Expected count - {expected_count}, but got {received_grades_stat.count}",
            )
        collector.verify_all_errors()


@allure.suite("Tests for grade statistics, average score")
class TestAverageGrade:
    @allure.title("Test grade average score for group")
    def test_grades_avg_for_group(
        self, university_service, grades_lst, student_group_with_marks
    ):
        with allure.step("Step 1: Receive grades statistics for group"):
            log.step(1, "Receive count of grades for group")
            received_stats = university_service.get_grades_statistics(
                group_id=student_group_with_marks
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for group"
        ):
            log.step(2, "Perform logic check, get average score for group")
            expected_stats = sum(grades_lst) / len(grades_lst)
            collector.check(
                expected_stats == received_stats.avg,
                f"Expected average score - {expected_stats}, but got {received_stats.avg}",
            )
        collector.verify_all_errors()

        collector.verify_all_errors()

    @allure.title("Test grade average score for student")
    def test_grade_avg_for_student(
        self, university_service, student_with_grades, grades_lst
    ):
        with allure.step("Step 1: Receive grades statistics for student"):
            log.step(1, "Receive grades statistics for student")
            received_stats = university_service.get_grades_statistics(
                student_id=student_with_grades
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for student"
        ):
            log.step(2, "Perform logic check, get average score for student")
            expected_stats = sum(grades_lst) / len(grades_lst)
            collector.check(
                expected_stats == received_stats.avg,
                f"Expected average score - {expected_stats}, but got {received_stats.avg}",
            )
        collector.verify_all_errors()

    @allure.title("Test grade average score for teacher")
    def test_grades_avg_for_teacher(self, university_service, teacher_and_grades):
        single_teacher, grades_values = teacher_and_grades
        with allure.step("Step 1: Receive grades statistics for teacher"):
            log.step(1, "Receive grades statistics for teacher")
            received_grades_stat = university_service.get_grades_statistics(
                teacher_id=single_teacher
            )
        with allure.step(
            "Step 2: Perform logic check, compare actual and received count for teacher"
        ):
            log.step(2, "Perform logic check, get average score for each teacher")
            expected_grades_avg = sum(grades_values) / len(grades_values)
            collector.check(
                expected_grades_avg == received_grades_stat.avg,
                f"Expected average score - {expected_grades_avg}, but got {received_grades_stat.avg}",
            )
        collector.verify_all_errors()
