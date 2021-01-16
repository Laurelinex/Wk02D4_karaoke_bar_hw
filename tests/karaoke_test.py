import unittest
from classes.karaoke import Karaoke
from classes.guest import Guest

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The Broadway Melodies", 10.00)
        self.guest = Guest("Carole Singer", 30.00)
    
    def test_karaoke_has_name(self):
        self.assertEqual("The Broadway Melodies", self.karaoke.name)
    
    def test_karaoke_has_entree_fee(self):
        self.assertEqual(10.00, self.karaoke.entry_fee)
    
    def test_guest_can_afford_entry(self):
        self.assertEqual(True, self.karaoke.guest_can_afford_entry(self.guest))

    def test_guest_cannot_afford_entry(self):
        a_not_wealthy_guy = Guest("Jeff Pesos", 2.00)
        self.assertEqual(False, self.karaoke.guest_can_afford_entry(a_not_wealthy_guy))