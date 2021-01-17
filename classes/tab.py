class Tab:

    def __init__(self):
        self.tabs = {}
        # intended: tabs = {guest: $spending}    
        # tabs[x]: returns the spending of x

    def add_guest_to_tab(self, guest):
        if guest not in self.tabs.keys():
            self.tabs[guest] = 0

    def add_to_guest_tab(self, guest, amount):
        if guest in self.tabs.keys():
            self.tabs[guest] += amount
        else: 
            return "This guest does not have a tab open."

    def check_amount_spent(self, guest):
        if guest in self.tabs.keys():
            return self.tabs[guest]
        else:
            return 0
        

