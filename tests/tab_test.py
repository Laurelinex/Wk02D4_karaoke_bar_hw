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