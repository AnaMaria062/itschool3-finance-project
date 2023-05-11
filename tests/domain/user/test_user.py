import unittest

from domain.user.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generated"
        user = User(username)
        # execution
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    def test_it_sets_the_stocks_we_give(self):
        username = "random-username"
        stocks = ['AMZN', 'MSFT', 'NVDA']
        user = User(username, stocks)

        actual_stocks = user.stocks

        self.assertEqual(stocks, actual_stocks)


if __name__ == "__main__":
    unittest.main()
