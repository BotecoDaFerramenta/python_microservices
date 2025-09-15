from domain.use_cases.add_account import AddAccount
from data.protocols.db.account.account_repository import AccountRepository


class DbAddAccount(AddAccount):
    def __init__(self, account_repository: AccountRepository):
        self.__account_repository = account_repository

    def create_unverified_account(self, new_account):
        return self.__account_repository.create_unverified_account(new_account)
