class User:
    # luokka, joka kuvaa yksittäistä käyttäjää
    def __init__(self, username, password):
        # username: merkkinojoarvo, joka kuvaa käyttäjän käyttäjätunnusta
        # password: merkkijonoarvo, joka kuvaa käyttäjän salasanaa
        self.username = username
        self.password = password