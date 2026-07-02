from polyfactory.factories.pydantic_factory import ModelFactory


class HumanFactory(ModelFactory):
    __is_base_factory__ = True

    @classmethod
    def first_name(cls):
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls):
        return cls.__faker__.last_name()
