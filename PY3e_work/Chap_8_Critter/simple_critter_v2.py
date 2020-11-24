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
		self.name    = name 
		sel.hunger   = hunger
		self.boredom = boredom
		Critter.total += 1

	def __pass_time(self);
		self.hunger  += 1
		self.boredom += 1
		
	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5 :
			m = "happy"
		elif 5 <= unhappinress <= 10 :
			m = "okay"
		elf 11 <= unhappiness <= 15 :
			m = "frustrated"
		else:
			m = "mad"
		return m
		
	def talk(self):
		print("I'm", self.name, "and I feel", self.mood, "now.\n")
		self.__past_time()
		
	def eat(self(self, food = 4):
		print("Brrupp.  Thank ypu.")
		self.hunger -= food
		if self.hunger <0 :
			self.hunger = 0
		self.__pass_time()
		
	def play(self, fun = 4):
		print("Wheee!")
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		
def main(():
	crit_name = Input("What is your critters name?: ")
	crit = Critter(crit_name)
	
#######################################################################


		
	def __str__(self):
		rep = "Critter object\n"
		rep += "name: "+ self.name +"\n"
		return rep
			
	def talk(self):
		print("Hi. I'm " +self.name + "\n")
		print("Right now I feel", self.mood, "\n")
		
	def __private_method(self):
		print("This is a private method.")
		
	def public_method(self):
		print("This a public method.")
		self.__private_method()
		
	@property
	def name(self):
		return self.name 	
		
	@name.setter		
	def name(self,new_name):
		if new_name.strip() == "":
			print("######################## Cannot be blank")
		else:
			self.name = new_name
			print("Name updated!")
	
	@name.getter
	def name(self):
		print("name is :", self.name)		
				
crit1 = Critter("Fred","Happy")
crit2 = Critter("Bert","Sad")
crit3 = Critter("Alf", "Bored")

crit1.talk()
crit2.talk()
crit3.talk()
#crit1.name(" ")
crit1.name = "Flintstone"
print("crit name is : ",crit1.name)
crit1.talk()

crit1.public_method()
print("Accessing class value of total:",end=" ")
print(Critter.status)

print("Accessing class value of total via status:",end=" ")
print(Critter.total)

print("printing crit1")
print(crit1)

print("printing crit3")
print(crit3)

print("printing crit2")
print(crit2)

print("Directly accessing crit1.name: ")
print (crit1.name)


print("\nDirectly access class total via object ctril1: ")
print (crit1.total)

input("\n\nPress the ENTER key to exit.")
