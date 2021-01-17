import unittest
from classes.guest import Guest
from classes.karaoke import Karaoke
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Carole Singer", 30.00)
        self.karaoke = Karaoke("The Broadway Melodies", 10.00)
        self.song = Song("Omigod You Guys", "Legally Blonde")
        self.room = Room(1, 5)
    
    def test_guest_has_name(self):
        self.assertEqual("Carole Singer", self.guest.name)
    
    def test_guest_has_money(self):
        self.assertEqual(30.00, self.guest.wallet)
    
    def test_guest_has_sufficient_funds_returns_true_if_enough(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.karaoke.entry_fee))
    
    def test_guest_has_sufficient_funds_returns_false_if_not_enough(self):
        a_not_wealthy_guy = Guest("Jeff Pesos", 2.00)
        self.assertEqual(False, a_not_wealthy_guy.sufficient_funds(self.karaoke.entry_fee))
    
    def test_guest_can_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.karaoke.entry_fee)
        self.assertEqual(20.00, self.guest.wallet)
    
    def test_guest_cannot_pay_entry_fee(self):
        a_not_wealthy_guy = Guest("Jeff Pesos", 2.00)
        a_not_wealthy_guy.pay_entry_fee(self.karaoke.entry_fee)
        self.assertEqual(2.00, a_not_wealthy_guy.wallet)
        self.assertEqual("You don't have enough cash.", a_not_wealthy_guy.pay_entry_fee(self.karaoke.entry_fee))
    
    def test_guest_can_choose_favourite_song(self):
        self.guest.choose_favourite_song(self.song.title)
        self.assertEqual("Omigod You Guys", self.guest.favourite_song)
    
    def test_guest_can_cheer_if_fav_song_in_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.guest.choose_favourite_song(self.song)
        self.guest.check_playlist_for_song(self.room.playlist, self.song)
        self.assertEqual("Whoo!", self.guest.check_playlist_for_song(self.room.playlist, self.song))
    
    def test_guest_complains_if_fav_song_not_in_playlist(self):
        a_song = Song("One Day More", "Les Misérables")
        self.room.add_song_to_playlist(self.song)
        self.guest.choose_favourite_song(a_song)
        self.guest.check_playlist_for_song(self.room.playlist, self.guest.favourite_song)
        self.assertEqual("This place sucks...", self.guest.check_playlist_for_song(self.room.playlist, self.guest.favourite_song))