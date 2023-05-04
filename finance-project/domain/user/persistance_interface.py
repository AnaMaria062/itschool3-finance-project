import abc
from uuid import UUID

from domain.user.user import User


class UserPersistenceInterface(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        pass

    @abc.abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abc.abstractmethod
    def delete(self, user_id: UUID):
        pass

    @abc.abstractmethod
    def edit(self, user_id: UUID, new_username: str):
        pass
