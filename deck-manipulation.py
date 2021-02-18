import random


def create_deck():
	
	suits = "SDCH"
	values = "23456789TJQKA"
	deck = []
	
	for suit in suits:
		for value in values:
			card = (value, suit)
			deck.append(card)
	
	return deck


def shuffle_deck(deck):
	
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)


def deal_deck(deck, player):
	if len(deck) == 1:
		card = deck.pop(0)
		deck = create_deck()
		shuffle_deck(deck)
		player.append(card)
		return deck
	
	else:
		card = deck.pop(0)
		player.append(card)
		return deck
	

deck = create_deck()
shuffle_deck(deck)
player1 = []
print(player1)
deal_deck(deck, player1)
print(player1)
