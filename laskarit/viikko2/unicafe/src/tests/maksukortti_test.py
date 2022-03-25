import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    def test_saldon_lisääminen_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    def test_saldo_vähenee_oikein(self):
        self.maksukortti.lataa_rahaa(190)
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    def test_rahat_riittävät(self):
        self.assertEqual((self.maksukortti.ota_rahaa(5)), True)
    def test_rahat_ei_riitä(self):
        self.assertEqual((self.maksukortti.ota_rahaa(15)), False)