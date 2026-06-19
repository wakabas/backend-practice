from random import randint

import pytest
from faker import Faker

from services.auth.factories.valid_user_factory import ValidUserFactory

faker = Faker()

password_arg_list = [
    {
        "length": randint(6, 7),
    },
    {
        "length": randint(100, 101),
        "special_chars": True,
        "digits": True,
        "upper_case": True
    },
    {
        "length": randint(8, 99),
        "special_chars": False,
        "digits": True,
        "upper_case": True
    },
    {
        "length": randint(8, 99),
        "special_chars": True,
        "digits": False,
        "upper_case": True
    }
]


@pytest.fixture(params=password_arg_list)
def invalid_user_creds(request):
    invalid_user = ValidUserFactory.build(password=faker.password(**request.param))
    return invalid_user
