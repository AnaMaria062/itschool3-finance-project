import logging
import json
import uuid
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo")
        self.__persistence = persistence
        self.logger = logging.getLogger(__name__)
        self.__users = None
        logging.basicConfig(filename='user_repo.log', level=logging.DEBUG)

    def __get_users(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()

    def add(self, new_user: User):
        self.__get_users()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__get_users()
        return self.__users

    def get_by_id(self, user_id: str) -> User:
        self.__get_users()
        for u in self.__users:
            if u.id == uuid.UUID(hex=user_id):
                assets = AssetRepo().get_for_user(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets
                )

        raise ValueError(f"No user found with id: {user_id}")

    def delete(self, user_id: str):
        user_to_delete = self.get_by_id(user_id)
        if user_to_delete:
            self.__users.remove(user_to_delete)
            users_info = [(str(x.id), x.username, x.stocks) for x in self.__users]
            users_json = json.dumps(users_info)
            file = open(self.file_path, "w")
            file.write(users_json)
            file.close()
            return True
        else:
            return False

    def get_user_with_info(self, user_id: str) -> User:
        user = self.get_by_id(user_id)
        if user:
            assets = AssetRepo().get_for_user(user)
            return User(
                uuid=user.id,
                username=user.username,
                stocks=assets
            )
        else:
            return User(uuid=uuid.UUID(int=0), username="", stocks=[])
