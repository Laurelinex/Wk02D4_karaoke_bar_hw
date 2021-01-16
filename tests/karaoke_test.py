import unittest
from classes.karaoke import Karaoke

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The Broadway Melodies", 10.00)
    
    def test_karaoke_has_name(self):
        self.assertEqual("The Broadway Melodies", self.karaoke.name)
    
    def test_karaoke_has_entree_fee(self):
        self.assertEqual(10.00, self.karaoke.entry_fee)