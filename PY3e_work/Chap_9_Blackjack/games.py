#!/usr/bin/env python3
''' 
**********************************************************************
* Filename      : games.py 
* Purpose       :Page 267 in PYe3
* Created       : 06 Dec 2020 
* Author        : Derek
**********************************************************************
* 
'''
class player(object):
	""" A player for a game """
	
	def __init__(self, name, score=0):
		self.name  = name
		self.score = score
	
	def __str__(self):
		rep = self.name + ":\t" + str(self.score)
		return rep
		
def ask_yes_no(question):
	response = None
	while response not in ("y","n"):
		response = input(question).lower()
	return response
	
def ask_number(question, low, high):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

if __name__ == "__main__":
	print("You ran this module directly and did not import it.")
	raw_input("\n\nPress the enter key to exit.")
	
