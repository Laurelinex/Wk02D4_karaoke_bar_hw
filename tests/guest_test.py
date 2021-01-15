import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ross Mills")
    
    def test_guest_has_name(self):
        self.assertEqual("Ross Mills", self.guest.name)