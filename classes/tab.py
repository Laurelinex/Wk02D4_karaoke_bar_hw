class Tab:

    def __init__(self):
        self.tabs = {}
    
    def add_guest_to_tab(self, guest):
        if guest not in self.tabs.keys():
            self.tabs[guest] = guest
    