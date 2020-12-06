#!/usr/bin/env python3
''' 
**********************************************************************
* Filename      : blackjack3.py
* Purpose       :Page 2672 in PYe3
* Created       : 06 Dec 2020 
* Author        : Derek
**********************************************************************
* 
'''
# Playing cards 3.0
# Demonstrates Inheritance

class Card(object):
	# A playing card
	RANKS = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
	SUITS = ["c","d","h","s"]

	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit
		
	def __str__(self):
		rep = self.rank + self.suit
		return rep

class UnPrintable_Card(Card):
	# a card that will not reveal its rank or suit when printed
	def __str__(self):
		return "<unprinttable>"
	
class Positionable_Card(Card):
	def __init__(self, rank, suit,face_up = True):
		super(Positionable_Card,self).__init__(rank,suit)
		self.is_faceup = face_up	
		
	def __str__(self):
		if self.is_faceup:
			rep = super(Positionable_Card, self).__str__()
		else:
			rep = "XX"
			
		return rep
		
	def flip(self):
		self.is_faceup = not self.is_faceup
########################################################################		
#main
card1 = Card("A","c")
card2 = UnPrintable_Card("A","d")
card3 = Positionable_Card("A","h")


print("\nPrinting a card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)

print("Flipping the positionable card object")
card3.flip()

print("Printing the positionable card object")
print(card3)
########################################################################		
