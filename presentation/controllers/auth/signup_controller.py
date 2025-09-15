from data.use_cases.db_add_account import DbAddAccount
from presentation.protocols.auth import Credentials
from presentation.protocols.http import HttpResponse
from presentation.protocols.controller import Controller

class SignUpController(Controller):
    def __init__(self, add_account: DbAddAccount):
        self.add_account = add_account.create_unverified_account

    def handle(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")

        if username is None or password is None:
            return HttpResponse(
                ok=False,
                status_code=400,
                message="invalid account credentials",
            )
        credentials = Credentials(username=username, password=password)
        response = self.add_account(new_account=credentials)

        status_code=201
        ok = response.get("ok")
        message=response.get("message")

        if ok is False:
            status_code=403

        return HttpResponse(
            ok=ok,
            status_code=status_code,
            message=message,
        )
