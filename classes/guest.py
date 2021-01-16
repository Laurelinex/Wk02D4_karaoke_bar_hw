class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def sufficient_funds(self, price):
        return self.wallet >= price
    
    def pay_entry_fee(self, entry_fee):
        if self.sufficient_funds(entry_fee):
            self.wallet -= entry_fee
        else: 
            return "You don't have enough cash."