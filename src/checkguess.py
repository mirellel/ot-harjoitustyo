from settings import *  # pylint: disable=unused-wildcard-import, disable=wildcard-import


class CheckGuess():
    def __init__(self):
        self.renderlist = ["", "", "", "", ""]
        self.guesscolourcode = [grey, grey, grey, grey, grey]

    def check(self, word, userquess):
        # tarkastaa, onko arvauksessa oikeita kirjaimia
        for i in range(0, 5):
            # oikea kirjain väärällä paikalla merkitään keltaisella
            if userquess[i] not in word:
                self.guesscolourcode[i] = grey
            if userquess[i] in word:
                self.guesscolourcode[i] = yellow
            # oikea kirjain oikealla paikalla merkitään vihreällä
            if userquess[i] == word[i]:
                self.guesscolourcode[i] = green
        list(userquess)
        # jos kaikki vihreää, voitto
        return self.guesscolourcode
