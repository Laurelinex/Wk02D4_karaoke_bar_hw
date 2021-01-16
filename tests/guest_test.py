import unittest
from classes.guest import Guest
from classes.karaoke import Karaoke

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Carole Singer", 30.00)
        self.karaoke = Karaoke("The Broadway Melodies", 10.00)
    
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