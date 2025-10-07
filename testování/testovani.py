import unittest
class Teplomer:
    def __init__(self, max_teplota=100):
        """Inicializuje objekt teploměru s výchozí teplotou 0 a maximální teplotou."""
        self.teplota = 0
        self.max_teplota = max_teplota

    def nastav_teplotu(self, nova_teplota):
        """Nastaví aktuální teplotu na hodnotu nova_teplota.
        Pokud přesáhne maximální teplotu, vyvolá výjimku."""
        if nova_teplota > self.max_teplota:
            raise ValueError("Teplota přesáhla maximální povolenou hodnotu!")
        self.teplota = nova_teplota

    def oteplit(self, stupne):
        """Zvýší teplotu o zadaný počet stupňů.
        Pokud výsledná teplota přesáhne maximální povolenou hodnotu, vyvolá výjimku."""
        if self.teplota + stupne > self.max_teplota:
            raise ValueError("Teplota přesáhla maximální povolenou hodnotu!")
        self.teplota += stupne

    def ochladit(self, stupne):
        """Sníží teplotu o zadaný počet stupňů.
        Teplota nesmí klesnout pod -273.15 °C."""
        nova_teplota = self.teplota - stupne
        self.teplota = max(nova_teplota, -273.15)

class TestTeplomer(unittest.TestCase):
    def test_inicializace(self):
        t1=Teplomer()
        self.assertEqual(t1.teplota, 0)
        self.assertEqual(t1.max_teplota, 100)


        t2 = Teplomer(max_teplota=150)  
        self.assertEqual(t2.teplota, 0)
        self.assertEqual(t2.max_teplota, 150)





if __name__ == '__main__':
    unittest.main()