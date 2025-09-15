from domain.models.account import Account
from data.protocols.db.account.account_repository import AccountRepository
from infra.db.nsql_mock.instance import DB_INSTANCE


class AccountRepositoryImpl(AccountRepository):
    def __init__(self):
        self.__valid_collection_name = "users"
        self.__pending_collection_name = "pending_users"
        self.__client = DB_INSTANCE

    def create_unverified_account(self, credentials: Account):
        valid_users = self.__client.get_collection(self.__valid_collection_name) or {}
        pending_users = (
            self.__client.get_collection(self.__pending_collection_name) or {}
        )
        username = credentials.username
        password = credentials.password

        response = dict()

        if valid_users.get(username) is not None:
            response["message"] = "account already exists"
            response["ok"] = False
            return response
        elif pending_users.get(username) is not None:
            response["message"] = "account awaiting validation"
            response["ok"] = False
            return response
        else:
            pass

        new_account = Account(username=username, password=password)
        self.__client.upsert(self.__pending_collection_name, username, new_account)
        response["message"] = "Account created. Please proceed to account validation."
        response["ok"] = True
        return response
