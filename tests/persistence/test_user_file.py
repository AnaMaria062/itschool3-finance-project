import unittest
import os
import tempfile
import uuid

from domain.user.user import User
from persistence.user_file import UserPersistenceFile


class TestUserPersistenceFile(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.user_persistence = UserPersistenceFile(self.temp_file.name)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_get_all(self):
        users = self.user_persistence.get_all()
        self.assertEqual(users, [])

        user1 = User(uuid.uuid4(), "user1", [])
        self.user_persistence.add(user1)
        users = self.user_persistence.get_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, user1.id)
        self.assertEqual(users[0].username, user1.username)
        self.assertEqual(users[0].stocks, user1.stocks)

        user2 = User(uuid.uuid4(), "user2", [])
        user3 = User(uuid.uuid4(), "user3", [])
        self.user_persistence.add(user2)
        self.user_persistence.add(user3)
        users = self.user_persistence.get_all()
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0].id, user1.id)
        self.assertEqual(users[0].username, user1.username)
        self.assertEqual(users[0].stocks, user1.stocks)
        self.assertEqual(users[1].id, user2.id)
        self.assertEqual(users[1].username, user2.username)
        self.assertEqual(users[1].stocks, user2.stocks)
        self.assertEqual(users[2].id, user3.id)
        self.assertEqual(users[2].username, user3.username)
        self.assertEqual(users[2].stocks, user3.stocks)


if __name__ == "__main__":
    unittest.main()
