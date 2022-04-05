import unittest
from checkguess import CheckGuess

class TestCheck(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_correct_word(self):
		checkGuess=CheckGuess()
		palautus=checkGuess.test_check("apple","apple")
		oikea=[(51,212,99),(51,212,99),(51,212,99),(51,212,99),(51,212,99)]
		self.assertEqual(palautus,oikea)
		
	
		
	
