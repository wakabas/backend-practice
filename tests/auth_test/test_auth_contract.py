import allure
import requests.status_codes
from faker import Faker

from services.auth.helpers.authentication_helper import AuthenticationHelper

faker = Faker()


@allure.suite("Tests for registration")
class TestRegisterContract:
    @allure.title("Valid registration test")
    def test_valid_register(self, auth_session_service_anonymous, valid_user_creds):
        register_helper = AuthenticationHelper(api_session=auth_session_service_anonymous)
        data = valid_user_creds.model_dump()
        register_response = register_helper.post_register(data=data)
        assert register_response.status_code == requests.status_codes.codes.created, (
            f"Expected code - {register_response.status_code}, but got {requests.status_codes.codes.created}"
        )

    @allure.title("Invalid registration test")
    def test_invalid_password_register(self, auth_session_service_anonymous, invalid_user_creds):
        register_helper = AuthenticationHelper(api_session=auth_session_service_anonymous)
        data = invalid_user_creds.model_dump()
        response = register_helper.post_register(data=data)
        assert requests.status_codes.codes.unprocessable == response.status_code, (
            f"Expected code - {requests.status_codes.codes.unprocessable}, but got {response.status_code}"
        )

    @allure.title("Test for registration with taken username")
    def test_taken_username(self, auth_session_service_anonymous, valid_user_creds):
        register_helper = AuthenticationHelper(api_session=auth_session_service_anonymous)
        doubled_user = valid_user_creds.model_dump()
        register_helper.post_register(data=doubled_user)
        doubled_register_response = register_helper.post_register(data=doubled_user)
        assert requests.status_codes.codes.conflict == doubled_register_response.status_code, (
            f"Expected code - {requests.status_codes.codes.conflict}, but got {doubled_register_response.status_code}"
        )
