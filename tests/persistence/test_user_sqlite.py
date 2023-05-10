import os
import unittest
import uuid
from unittest.mock import patch, MagicMock
from domain.user.user import User
from persistence.user_sqlite import UserPersistenceSqlite


class TestUserPersistenceSqlite(unittest.TestCase):
    def setUp(self):
        self.test_user = User(uuid.uuid4(), "test_username")

    def tearDown(self):
        if os.path.exists("main_users.db"):
            os.remove("main_users.db")

    @patch("sqlite3.connect")
    def test_add(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        persistence = UserPersistenceSqlite()
        persistence.add(self.test_user)

        mock_cursor.execute.assert_called_once_with(
            f"INSERT INTO users (id, username) VALUES ('{self.test_user.id}', '{self.test_user.username}')"
        )

    @patch("sqlite3.connect")
    def test_delete(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        persistence = UserPersistenceSqlite()
        persistence.delete(self.test_user.id)

        mock_cursor.execute.assert_called_once_with(
            f"DELETE FROM users WHERE id='{self.test_user.id}'"
        )

    @patch("sqlite3.connect")
    def test_edit(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        persistence = UserPersistenceSqlite()
        persistence.edit(self.test_user.id, "new_username")

        mock_cursor.execute.assert_called_once_with(
            f"UPDATE users SET username='new_username' WHERE id='{self.test_user.id}'"
        )


if __name__ == '__main__':
    unittest.main()
