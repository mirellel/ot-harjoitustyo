import unittest
from entities.user import User
from services.game_service import (
    GameService, InvalidCredentialsError, UsernameExistsError)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.service = GameService(FakeUserRepository())

        self.user_miiris = User('miiris', 'fili123')

    def login_user(self, user):
        self.service.create(user.username, user.password)

    def test_login_with_valid_credentials(self):
        self.service.create(
            self.user_miiris.username,
            self.user_miiris.password
        )

        user = self.service.login(
            self.user_miiris.username,
            self.user_miiris.password
        )

        self.assertEqual(user.username, self.user_miiris.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.service.login("test", "invalid"))

    def test_create_user_unsuccessfully(self):
        username = self.user_miiris.username

        self.service.create(username, 'invalid')

        self.assertRaises(UsernameExistsError,
                          lambda: self.service.create(username, "something"))

    def test_current_user(self):
        self.login_user(self.user_miiris)

        current = self.service.get_current_user()

        self.assertEqual(current.username, self.user_miiris.username)
