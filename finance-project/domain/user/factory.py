import uuid
from domain.user.user import User
import re


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        if len(username) > 20:
            raise InvalidUsername("Username should be no more than 20 characters")
        pattern = r"^[a-zA-Z0-9_-]+$"
        if not re.match(pattern, username):
            raise InvalidUsername(
                "Username should contain only alphanumeric characters, underscores, or dashes"
            )
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistance(self, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
        )
