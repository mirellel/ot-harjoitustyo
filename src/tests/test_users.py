import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user1 = User("mirelle", "mirkku123", 0, 0)
        self.user2 = User("aarni", "salasana1", 0, 0)
        self.user3 = User("kalle", "kalle123", 1, 1)

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

    def test_get_wins(self):
        user_repository.create(self.user1)
        wins = user_repository.get_games_won(self.user1.username)
        self.assertEqual(wins, self.user1.games_won)
    
    def test_get_plays(self):
        user_repository.create(self.user1)
        plays = user_repository.get_games_won(self.user1.username)
        self.assertEqual(plays, self.user1.games_won)

    def test_update_wins(self):
        user_repository.create(self.user3)
        user_repository.update_games_won(self.user3.username)
        wins = user_repository.get_games_won(self.user3.username)
        self.assertEqual(wins, self.user3.games_won)

    def test_update_plays(self):
        user_repository.create(self.user3)
        user_repository.update_games_played(self.user3.username)
        plays = user_repository.get_games_played(self.user3.username)
        self.assertEqual(plays, self.user3.games_won)

