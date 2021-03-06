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

	values = ["23456789TJQKA"]

	def __init__(self):
		super().__init__(1)
		self.player1 = []
		self.player2 = []
		self.tribute1 = None
		self.tribute2 = None
		self.war_tribute = None

	def set_up_game(self):
		for card in self.shoe:
			if len(self.shoe) == 0:
				print("Players Dealt")
			else:
				self.player1.append(card)
				self.player2.append(card)

	def collect_tribute(self):
		self.tribute1 = self.player1.pop(0)
		self.tribute2 = self.player2.pop(0)

	def collect_war_tribute(self):
		self.war_tribute = []
		for i in range(3):
			foo = []
			foo.append(self.player1.pop())
			foo.append(self.player2.pop())
			self.war_tribute = self.war_tribute + foo

	def compare_tributes(self):
		val1 = self.tribute1[0]
		val2 = self.tribute2[0]
		if War.values.index(val1) > War.values.index(val2):
			self.player1.append(self.tribute2)
			self.player1.append(self.tribute1)
		elif War.values.index(val1) > War.values.index(val2):
			self.player2.append(self.tribute2)
			self.player2.append(self.tribute1)
		else:
			print("WAR!")

deck = Deck(1)
