from pydantic import BaseModel
from domain.models.account import Account

class AddAccountResponse(BaseModel):
    ok: bool
    message: str

class AddAccount:
    def create_unverified_account(self, credentials: Account) -> AddAccountResponse:
        pass
