class Karaoke:
     
    def __init__(self, name, entry_fee):
        self.name = name
        self.entry_fee = entry_fee
        self.rooms = []
        
    def guest_can_afford_entry(self, guest):
        return guest.sufficient_funds(self.entry_fee)