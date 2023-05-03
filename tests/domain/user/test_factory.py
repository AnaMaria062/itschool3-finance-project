import unittest

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_a_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20"
        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6_chars(self):
        username = "below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username should have at least 6 characters", str(context.exception)
        )

    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "this-username-is-above-20-chars"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username should be no more than 20 characters", str(context.exception)
        )

    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        valid_usernames = ["user_name", "user1234", "user-name"]
        for username in valid_usernames:
            factory = UserFactory()

            actual_user = factory.make_new(username)

            self.assertEqual(username, actual_user.username)
            self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        invalid_usernames = ["user$name*invalid", "&username", "u@ser"]
        factory = UserFactory()

        for username in invalid_usernames:
            with self.assertRaises(InvalidUsername) as context:
                factory.make_new(username)
            self.assertEqual(
                type(context.exception),
                InvalidUsername,
                "Username should contain only alphanumeric characters, underscores, or dashes",
            )


if __name__ == "__main__":
    unittest.main()
