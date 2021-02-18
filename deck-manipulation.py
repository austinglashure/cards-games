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

deck = create_deck()

