class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.favourite_song = ""
    
    def sufficient_funds(self, price):
        return self.wallet >= price
    
    def pay_entry_fee(self, entry_fee):
        if self.sufficient_funds(entry_fee):
            self.wallet -= entry_fee
        else: 
            return "You don't have enough cash."
    
    def choose_favourite_song(self, song):
        self.favourite_song = song
    
    def check_playlist_for_song(self, playlist, song):
        if song in playlist:
            return "Whoo!"
        else:
            return "This place sucks..."