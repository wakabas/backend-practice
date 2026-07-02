from services.general.factories.human_factory import HumanFactory
from services.university.models.student_post_request import StudentPostRequest


class StudentFactory(HumanFactory):
    __model__ = StudentPostRequest

    @classmethod
    def phone(cls):
        return cls.__faker__.numerify("+7##########")
