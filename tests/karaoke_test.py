import unittest
from classes.karaoke import Karaoke

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The Broadway Melodies")
    
    def test_karaoke_has_name(self):
        self.assertEqual("The Broadway Melodies", self.karaoke.name)