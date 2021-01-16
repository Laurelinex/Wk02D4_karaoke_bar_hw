import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1)
        self.guest = Guest("Carole Singer")
    
    def test_room_has_room_number(self):
        self.assertEqual(1, self.room.room_number)
    
    def test_room_guests_list_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))