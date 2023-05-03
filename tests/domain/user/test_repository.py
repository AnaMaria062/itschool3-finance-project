import unittest

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.repo import UserRepo


class UserRepositoryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.users_file = "test_users.json"
        cls.repo = UserRepo(cls.users_file)

    def test_it_adds_a_user(self):
        expected_username = "a-username"
        new_user = UserFactory().make_new(expected_username)

        self.repo.add(new_user)

        actual_users = self.repo.get_all()
        self.assertEqual(1, len(actual_users))
        self.assertEqual(expected_username, actual_users[0].username)

    def test_it_reads_a_user_from_the_system(self):
        repo = UserRepo(self.users_file)

        actual_users = repo.get_all()

        self.assertEqual(1, len(actual_users))

    def test_it_handles_short_usernames(self):
        with self.assertRaises(InvalidUsername):
            UserFactory().make_new("short")

    def test_it_handles_long_usernames(self):
        with self.assertRaises(InvalidUsername):
            UserFactory().make_new("averylongusernameover20characters")

    def test_it_handles_invalid_characters_in_usernames(self):
        with self.assertRaises(InvalidUsername):
            UserFactory().make_new("invalid!username")

    def test_it_handles_valid_usernames(self):
        new_user_1 = UserFactory().make_new("user12")
        new_user_2 = UserFactory().make_new("user-2")
        new_user_3 = UserFactory().make_new("user_3")
        new_user_4 = UserFactory().make_new("user4_")

        self.assertEqual(new_user_1.username, "user12")
        self.assertEqual(new_user_2.username, "user-2")
        self.assertEqual(new_user_3.username, "user_3")
        self.assertEqual(new_user_4.username, "user4_")


if __name__ == "__main__":
    unittest.main()
