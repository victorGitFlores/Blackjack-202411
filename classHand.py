#classHand.py

class Hand:
	def __init__(self):
		self.reset_hand()
	
	def reset_hand(self):
		self.cards = []
		self.value1 = 0
		self.value11 = 0

	def add_card(self, card):
		self.cards.append(card)
		self.recalc_hand_values()

	# think i need this, no?  ... maybe not
	def deal_from_hand(self):
		w_card = None
		if self.cards:
			w_card = self.cards.pop(0)
			self.recalc_hand_values(self)						
		return w_card

	def recalc_hand_values(self):
		w_val1 = 0
		w_val11 = 0
		for c in self.cards:
			w_val1  += 1  if c.rank == "Ace" else c.value
			w_val11 += 11 if c.rank == "Ace" else c.value
		self.value1 = w_val1
		self.value11 = w_val11
