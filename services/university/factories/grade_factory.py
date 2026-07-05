from polyfactory.factories.pydantic_factory import ModelFactory

from services.university.models.grade_post_request import GradePostRequest


class GradeFactory(ModelFactory):
    __model__ = GradePostRequest

    @classmethod
    def teacher_id(cls, teacher_id: int):
        return teacher_id

    @classmethod
    def student_id(cls, student_id: int):
        return student_id
