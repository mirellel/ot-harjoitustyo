'''importataan tarvittavat värit'''
from settings import grey, yellow, green

class CheckGuess(): # pylint: disable=too-few-public-methods
    '''Pelilogiikasta vastaavaluokka'''

    def __init__(self):
        '''luokan konstruktori
        '''
        self.renderlist = ["", "", "", "", ""]
        self.guesscolourcode = [grey, grey, grey, grey, grey]

    def check(self, word, userguess):
        """Luo uuden tehtävän.
        Args:
            word: Merkkijonoarvo, joka kuvaa voittosanaa.
            userguess: Merkkijonoarvo, joka kuvaa käyttäjän syöttämää arvausta
        Returns:
            Käyttäjän arvauksen värikoodin listamuodossa.
        """
        for i in range(0, 5):
            if userguess[i] not in word:
                self.guesscolourcode[i] = grey
            if userguess[i] in word:
                self.guesscolourcode[i] = yellow
            if userguess[i] == word[i]:
                self.guesscolourcode[i] = green
        list(userguess)
        return self.guesscolourcode
