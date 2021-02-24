import random


class Deck:

	def __init__(self, no_of_decks):

		suits = "SDCH"  # Spades, Diamonds, Clubs, Hearts
		faces = "23456789TJQKA"
		self.shoe = []  # a fancy name for a deck of multiple decks
		for dck in range(no_of_decks):
			self.deck = []
			for suit in suits:
				for face in faces:
					self.card = face + suit
					self.deck.append(self.card)
			random.shuffle(self.deck)
			self.shoe += self.deck

	def deal_card(self):
		return self.shoe.pop(0)

	def show_deck(self):
		for card in self.shoe:
			print(card)


deck = Deck(1)
