import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Carole Singer", 30.00)
    
    def test_guest_has_name(self):
        self.assertEqual("Carole Singer", self.guest.name)
    
    def test_guest_has_money(self):
        self.assertEqual(30.00, self.guest.wallet)