import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user1 = User("mirelle", "mirkku123")
        self.user2 = User("aarni", "salasana1")

    def test_create(self):
        user_repository.create(self.user1)
        all = user_repository.find_all()
        self.assertEqual(all[0].username, self.user1.username)

    def test_find_users(self):
        user_repository.create(self.user1)
        user_repository.create(self.user2)
        all = user_repository.find_all()
        self.assertEqual(all[0].username, self.user1.username)
        self.assertEqual(all[1].username, self.user2.username)

    def test_find_by_username(self):
        user_repository.create(self.user2)
        user = user_repository.find_by_username(self.user2.username)
        self.assertEqual(user.username, self.user2.username)
