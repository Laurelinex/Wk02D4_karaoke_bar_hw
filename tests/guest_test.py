import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Carole Singer")
    
    def test_guest_has_name(self):
        self.assertEqual("Carole Singer", self.guest.name)