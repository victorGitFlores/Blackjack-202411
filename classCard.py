#classCard.py

class Card:
	def __init__(self, suit, rank, value ):
		self.suit  = suit
		self.rank  = rank
		self.value = value

	def __str__(self):
		return f"{self.rank} of {self.suit} ... value: {self.value}"

	def print_card(self, face_up):
		if face_up:
			print(f"{self.rank} of {self.suit}")
		else:
			print(f"BLACKJACK CASINO LAS VEGAS, NV")	

