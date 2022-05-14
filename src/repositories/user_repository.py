from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self._connection = get_database_connection()


    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.
        Args:
            todo: Tallennettava käyttäjä User-oliona.
        Returns:
            Tallennettu käyttjä User-oliona.
        """
        username = user.username.lower()
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password, games_won, games_played) values (?, ?, ?, ?)",
            (username, user.password, 0, 0)
        )

        self._connection.commit()
        return user

    def tuple_to_user(self, user):
        '''apufunktio, joka muuttaa tuplen User-olioksi
        Args:
            user: tuple, joka sisältää halutun User-olion kentät
        Returns:
            User-olio
        '''
        if not user:
            return None
        user_return = User(user[0], user[1], user[2], user[3])

        return user_return

    def find_all(self):
        """Palauttaa kaikki käyttäjät.
        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self._connection.cursor()
        cursor.execute('select * from users')

        fetch_users = cursor.fetchall()

        fetch_users = map(self.tuple_to_user, fetch_users)

        return list(fetch_users)

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.
        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omaava käyttäjä on tietokannassa.
            Muussa tapauksessa None.
        """
        if not username:
            return None
        cursor = self._connection.cursor()

        cursor.execute(
            "select username, password, games_won, games_played from users where username = ?",
            [username]
        )
        user = cursor.fetchone()

        return self.tuple_to_user(user)

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM USERS')

        self._connection.commit()

    def get_games_won(self, username):
        '''Hakee tietokannasta kirjautuneen pelaajan sen hetkisen voittojen määrän
        Args:
            username: pelaajan käyttäjänimi
            
        Returns:
            palauttaa pelaajan voitettujen pelien määrän'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT games_won from users WHERE username = ?', [username])
        games_won = cursor.fetchone()[0]

        return games_won

    def get_games_played(self, username):
        '''Hakee tietokannasta kirjautuneen pelaajan sen hetkisen pelien määrän
        Args:
            username: pelaajan käyttäjänimi
            
        Returns:
            palauttaa pelaajan pelattujen pelien määrän'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT games_played from users WHERE username = ?', [username])
        games_played = cursor.fetchone()
        games_played = games_played[0]

        return games_played

    def update_games_won(self, username):
        '''Päivittää pelaajan voitettujen pelien määrän tietokantaan
        Args:
            username: pelaajan käyttäjänimi 
        '''
        cursor = self._connection.cursor()
        games_won_new = self.get_games_won(username)+1
        
        cursor.execute("UPDATE users SET games_won=? WHERE username=?",
            (games_won_new, username))
        self._connection.commit()

    def update_games_played(self, username):
        '''Päivittää pelaajan pelattujen pelien määrän tietokantaan
        Args:
            username: pelaajan käyttäjänimi 
        '''
        cursor = self._connection.cursor()
        games_played_new = self.get_games_played(username)+1
        cursor.execute("UPDATE users SET games_played=? WHERE username=?",
            (games_played_new, username))
        self._connection.commit()

user_repository = UserRepository()
users = user_repository.find_all()
