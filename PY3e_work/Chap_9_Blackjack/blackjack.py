#!/usr/bin/env python3
''' 
**********************************************************************
* Filename      : blackjack.py
* Purpose       : ACCESS CONTROL -- hide passwords
* Created       : 27 Nov 2020 
* Author        : Derek
**********************************************************************
* 
'''
# Alien Blaster
# Show object interaction

class player(object):
	def blast(self,enemy):
		print("The player blasts an enemy.\n")
		enemy.die()
		
class Alien(object):		
	def die(self):
		print("Te alien gasps and says, 'Oh, this is it. This is the big one. \n" \
			"Yes, its getting dark  now. \n" \
			"Good Bye'")
				
hero    = player()
invader = Alien()

hero.blast(invader)

raw_input ("\n\nPress enter key to exit.")
