from services.general.factories.human_factory import HumanFactory
from services.university.models.teacher_post_request import TeacherPostRequest


class TeacherFactory(HumanFactory):
    __model__ = TeacherPostRequest
