import unittest
from classes.tab import Tab
from classes.guest import Guest

class TestTab(unittest.TestCase):

    def setUp(self):
        self.tab = Tab()
        self.guest = Guest("Amanda Lynn", 40.00)
    
    def test_tabs_start_empty(self):
        self.assertEqual(0, len(self.tab.tabs))
    
    def test_tab_can_add_guest(self):
        self.tab.add_guest_to_tab(self.guest)
        self.assertEqual(1, len(self.tab.tabs))
    
    def test_tab_can_check_amount_spent(self):
        self.tab.check_amount_spent(self.guest)
        self.assertEqual(0, self.tab.check_amount_spent(self.guest))
    
    def test_tab_can_add_amount_to_guest_tab(self):
        some_amount = 5.00
        self.tab.add_guest_to_tab(self.guest)
        self.tab.add_to_guest_tab(self.guest, some_amount)
        self.assertEqual(5.00, self.tab.check_amount_spent(self.guest))