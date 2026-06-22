from services.general.base_service import BaseService
from services.general.models.success_response import SuccessResponse
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade_post_request import GradePostRequest
from services.university.models.grade_post_response import GradePostResponse
from services.university.models.grade_statistics_request import GradeStatisticsRequest
from services.university.models.grade_statistics_response import GradeStatisticsResponse
from services.university.models.group_delete_request import GroupDeleteRequest
from services.university.models.group_post_request import GroupPostRequest
from services.university.models.group_post_response import GroupPostResponse
from services.university.models.student_delete_request import StudentDeleteRequest
from services.university.models.student_post_request import StudentPostRequest
from services.university.models.student_post_response import StudentPostResponse
from services.university.models.teacher_delete_request import TeacherDeleteRequest
from services.university.models.teacher_post_request import TeacherPostRequest
from services.university.models.teacher_post_response import TeacherPostResponse
from utils.api_session import ApiSession


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_session: ApiSession):
        super().__init__(api_session)
        self.grade_helper = GradeHelper(self.api_session)
        self.group_helper = GroupHelper(self.api_session)
        self.student_helper = StudentHelper(self.api_session)
        self.teacher_helper = TeacherHelper(self.api_session)

    def create_student(self, student_request: StudentPostRequest) -> StudentPostResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentPostResponse(**response.json())

    def create_multiple_students(self, student_requests: list[StudentPostRequest]) -> list[
        StudentPostResponse]:
        return [self.create_student(student_request) for student_request in student_requests]

    def delete_student(self, student_request: StudentDeleteRequest) -> SuccessResponse:
        response = self.student_helper.delete_student(student_request.student_id)
        return SuccessResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherPostRequest) -> TeacherPostResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherPostResponse(**response.json())

    def create_multiple_teachers(self, teacher_requests: list[TeacherPostRequest]) -> list[TeacherPostResponse]:
        return [self.create_teacher(teacher_request) for teacher_request in teacher_requests]

    def delete_teacher(self, teacher_request: TeacherDeleteRequest) -> SuccessResponse:
        response = self.teacher_helper.delete_teacher(teacher_request.teacher_id)
        return SuccessResponse(**response.json())

    def create_group(self, group_request: GroupPostRequest) -> GroupPostResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupPostResponse(**response.json())

    def delete_group(self, group_request: GroupDeleteRequest) -> SuccessResponse:
        response = self.group_helper.delete_group(group_request.group_id)
        return SuccessResponse(**response.json())

    def create_grade(self, grade_request: GradePostRequest) -> GradePostResponse:
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradePostResponse(**response.json())

    def create_multiple_grades(self, grade_requests: list[GradePostRequest]) -> list[GradePostResponse]:
        return [self.create_grade(grade_request) for grade_request in grade_requests]

    def get_grades_statistics(self, group_id: int | None = None,
                                    student_id: int | None = None,
                                    teacher_id: int | None = None) -> GradeStatisticsResponse:
        response = self.grade_helper.get_stats(group_id=group_id,
                                               student_id=student_id,
                                               teacher_id=teacher_id)
        return GradeStatisticsResponse(**response.json())
