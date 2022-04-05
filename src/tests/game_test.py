import unittest
from checkguess import CheckGuess

class TestCheck(unittest.TestCase):
	def setUp(self):
		pass
		
		
	def test_correct_word(self):
		palautus=checkGuess.test_check("apple","apple")
		self.assetEqual(palautus,["green","green","green","green","green"])
		
	
