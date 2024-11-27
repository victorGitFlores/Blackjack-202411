# Deck.py

import classCard
import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = (
	{"Two":2, "Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
	 "Jack":10,"Queen":10,"King":10,"Ace":11 
	}
	)


class Deck:
	# class attribs
	#deck_stack = []
	#methods
	def __init__(self): #create a deck with 52 cards
		self.init_deck()

	def init_deck(self):
		self.deck_stack = []
		for suit in suits:
			for rank in ranks:
				self.deck_stack.append(classCard.Card(suit, rank, values[rank]))
		self.shuffle()


	def shuffle(self):
		random.shuffle(self.deck_stack)

	def deal_one(self):
		'''
		   returns a card from the deck, or None if deck empty
		'''
		try:
			one_card = self.deck_stack.pop(0)
			if len(self.deck_stack) == 0:
				init_deck()
			print(f"just dealt a {one_card.rank}")
			return one_card
		except:
			return None
