from services.general.base_service import BaseService
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from utils.api_session import ApiSession


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, session: ApiSession):
        super().__init__(session)
        self.grade_helper = GradeHelper(self.session)
        self.group_helper = GroupHelper(self.session)
        self.student_helper = StudentHelper(self.session)
        self.teacher_helper = TeacherHelper(self.session)

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(student_request.model_dump())
        return StudentResponse(**response.json())

