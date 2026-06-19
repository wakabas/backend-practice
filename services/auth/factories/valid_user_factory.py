from polyfactory.factories.pydantic_factory import ModelFactory

from services.auth.models.register_request import RegisterRequest


class ValidUserFactory(ModelFactory):
    __model__ = RegisterRequest

    @classmethod
    def username(cls):
        return cls.__faker__.user_name()

    @classmethod
    def password(cls):
        return cls.__faker__.password(length=20,
                                      special_chars=True,
                                      digits=True,
                                      upper_case=True,
                                      lower_case=True, )

    @classmethod
    def build(cls, **kwargs):
        if "password" in kwargs and "password_repeat" not in kwargs:
            kwargs["password_repeat"] = kwargs["password"]

        res = super().build(**kwargs)

        if "password_repeat" not in kwargs:
            res.password_repeat = res.password

        return res
