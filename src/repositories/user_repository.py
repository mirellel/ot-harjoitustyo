from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None

class UserRepository:
    # käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):
        # palauttaa kaikki käyttäjät

        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM USERS')

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        # palauttaa käyttäjän käyttäjätunnuksen perusteella
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        # tallentaa käyttäjän tietokantaan

        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO USERS (username, password) values (?, ?)',
            (user.username, user.password)
        )

        self._connection.commit()
        return user

    def delete_all(self):
        #poistaa kaikki käyttäjät

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM USERS')

        self._connection.commit()

user_repository = UserRepository(get_database_connection())