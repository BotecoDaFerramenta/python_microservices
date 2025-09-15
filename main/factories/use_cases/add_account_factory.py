from data.use_cases.db_add_account import DbAddAccount
from infra.db.nsql_mock.account_repository import AccountRepositoryImpl


def create_add_account():
    account_repository = AccountRepositoryImpl()
    return DbAddAccount(account_repository)
