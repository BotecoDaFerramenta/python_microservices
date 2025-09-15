from main.factories.use_cases.add_account_factory import create_add_account
from presentation.controllers.auth.signup_controller import SignUpController


def create_signup_controller():
    return SignUpController(create_add_account())
