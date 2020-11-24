#!/usr/bin/env python3

# PY3e page 220 & onwards in Chap 8

class Critter(object):
	
	total = 0
	
	@staticmethod
	def status():
		print ("\nTotal number critters is:", Critter.total)
		print
		
	""" virtual Pet"""
	def __init__(self, name, hunger = 0, boredom = 0  ):
		print("A new  critter has been born!")
		self.name     = name 
		self.hunger   = hunger
		self.boredom  = boredom
		Critter.total += 1

	def __pass_time(self):
		self.hunger  += 1
		self.boredom += 1
		
	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		print("Happy value= "+str(unhappiness))
		if unhappiness < 5 :
			m = "happy"
		elif 5 <= unhappiness <= 10 :
			m = "okay"
		elif 11 <= unhappiness <= 15 :
			m = "frustrated"
		else:
			m = "mad"
		return m
		
	def eat(self, food = 4):
		print("Brrupp.  Thank ypu.")
		self.hunger -= food
		if self.hunger <0 :
			self.hunger = 0
		self.__pass_time()
	
	def talk(self):
		print("I'm", self.name, "and I feel", self.mood, "now.\n")	
	
	def play(self, fun = 4):
		print("Wheee!")
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		
def main():
	crit_name = input("What is your critters name?: ")
	crit = Critter(crit_name)
	choice = None
	while choice != "0":
		print \
		("""
		Critter Caretaker
		
		o - Quit
		1 - Listen to your critter
		2 - Feed your critter
		3 - Play withyour critter
		""")

		choice = input("Choice: ")
		print()
		
		if choice == "0":
			print("Good Bye.")
		elif choice == "1":
			crit.talk()
		elif choice == "2":
			crit.eat()
		elif choice == "3":
			crit.play()
		else:
			print("Invalid choice!!")		
#######################################################################
if __name__ == "__main__":
	main()
