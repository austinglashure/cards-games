import random


def show_deck(shoo):
	for card in shoo:
		print(card)


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


class War(Deck):

	def __init__(self):
		super().__init__(1)
		self.player1 = []
		self.player2 = []

	def set_up_game(self):
		for card in self.shoe:
			if len(self.shoe) == 0:
				print("Players Dealt")
			else:
				self.player1.append(card)
				self.player2.append(card)

	def collect_tribute(self):





deck = Deck(1)
