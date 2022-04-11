import unittest
from checkguess import CheckGuess
checkGuess = CheckGuess()


class TestCheck(unittest.TestCase):
    def setUp(self):
        pass

    def test_correct_word(self):
        checkGuess = CheckGuess()
        palautus = checkGuess.check("apple", "apple")
        oikea = [(51, 212, 99), (51, 212, 99), (51, 212, 99),
                 (51, 212, 99), (51, 212, 99)]
        self.assertEqual(palautus, oikea)

    def test_incorrect_word(self):
        checkGuess = CheckGuess()
        palautus = checkGuess.check("apple", "grout")
        oikea = [(127, 128, 122), (127, 128, 122), (127, 128, 122),
                 (127, 128, 122), (127, 128, 122)]
        self.assertEqual(palautus, oikea)

    def test_partially_correct_word(self):
        checkGuess = CheckGuess()
        palautus = checkGuess.check("apple", "april")
        oikea = [(51, 212, 99), (51, 212, 99), (127, 128, 122),
                 (127, 128, 122), (222, 224, 81)]
        self.assertEqual(palautus, oikea)
