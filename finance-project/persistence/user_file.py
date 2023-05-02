import json
import logging

from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User


class UserPersistenceFile(UserPersistenceInterface):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.logger = logging.getLogger(__name__)

    def get_all(self) -> list[User]:
        try:
            with open(self.__file_path) as contents:
                users_info = json.load(contents)
                factory = UserFactory()
                return [factory.make_from_persistance(x) for x in users_info]
        except Exception as e:
            self.logger.error(f"Failed to load users from file {self.__file_path}: {e}")
            return []

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        with open(self.__file_path, "w") as f:
            json.dump(users_info, f)
