#classChips.py

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet 
        self.bet = 0
    
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

    def set_bet(self, bet):
        # bet will never be zero (this function not called)
        if bet <= self.total:
            self.bet = bet
            print(f"Bet for {bet} has been placed!")
            return True # bet placed
        else:
            return False # bet not placed


