import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Defying Gravity", "Wicked")
    
    def test_song_has_title(self):
        self.assertEqual("Defying Gravity", self.song.title)
    
    def test_song_has_musical_name(self):
        self.assertEqual("Wicked", self.song.musical)
