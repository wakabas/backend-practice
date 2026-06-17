import pytest
import requests.status_codes
from faker import Faker

from services.auth.helpers.authentication_helper import AuthenticationHelper

faker = Faker()


class TestRegisterContract:

    def test_valid_register(self, auth_session_service_anonymous, valid_user_creds):
        register_helper = AuthenticationHelper(api_session=auth_session_service_anonymous)
        register_response = register_helper.post_register(data={"username": valid_user_creds.username,
                                                           "password": valid_user_creds.password,
                                                           "password_repeat": valid_user_creds.password,
                                                           "email": faker.email()})
        assert register_response.status_code == requests.status_codes.codes.created, \
            f"Expected code - {register_response.status_code}, but got {requests.status_codes.codes.created}"

    def test_invalid_register(self, auth_session_service_anonymous, invalid_user_creds):
        register_helper = AuthenticationHelper(api_session=auth_session_service_anonymous)
        register_response = register_helper.post_register(data={"username": invalid_user_creds.username,
                                                                "password": invalid_user_creds.password,
                                                                "password_repeat": invalid_user_creds.password,
                                                                "email": faker.email()})
        assert register_response.status_code == requests.status_codes.codes.unprocessable, \
            f"Expected code - {requests.status_codes.codes.unprocessable}, but got {register_response.status_code}"