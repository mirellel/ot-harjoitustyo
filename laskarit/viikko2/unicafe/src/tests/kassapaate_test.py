import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(1000)

    def test_rahamaara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounauden_maara_alussa(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_maukas_käteisellä(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_käteisellä(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisella_edullinen_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_maukas_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_kateisella_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_kortilla_lounas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(999)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 1)
        self.maksukortti.ota_rahaa(999)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 1)

    def test_kassan_rahamäärä_ei_muutu_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladataan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_ladataan_negatiivista_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    