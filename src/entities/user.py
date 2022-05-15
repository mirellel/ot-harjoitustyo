'''Docstring'''
class User:
    '''luokka, joka kuvaa yksittäistä käyttäjää'''
    def __init__(self, username, password, games_won, games_played):
        """Luokan konstruktori, joka luo uuden käyttäjän.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
            games_won: lukuarvo, joka kuvaa käyttäjän voittamien pelien määrää
            games_played: lukuarvo, joka kuvaa käyttäjän pelaamien pelien määrää
        """
        self.username = username
        self.password = password
        self.games_won = games_won
        self.games_played = games_played
