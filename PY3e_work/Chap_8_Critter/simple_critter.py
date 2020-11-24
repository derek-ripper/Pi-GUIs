#!/usr/bin/env python3

# PY3e page 220 & onwards in Chap 8

class Critter(object):
	
	total = 0
	
	@staticmethod
	def status():
		print ("\nTotal number critters is:", Critter.total)
		print
		
	""" virtual Pet"""
	def __init__(self, name, mood ):
		print("A new  critter has been born!")
		self.__name   = name 
		self.__mood = mood
		Critter.total += 1

		
	def __str__(self):
		rep = "Critter object\n"
		rep += "name: "+ self.__name +"\n"
		return rep
			
	def talk(self):
		print("Hi. I'm " +self.__name + "\n")
		print("Right now I feel", self.__mood, "\n")
		
	def __private_method(self):
		print("This is a private method.")
		
	def public_method(self):
		print("This a public method.")
		self.__private_method()
		
	@property
	def name(self):
		return self.__name 	
		
	@name.setter		
	def name(self,new_name):
		if new_name.strip() == "":
			print("######################## Cannot be blank")
		else:
			self.__name = new_name
			print("Name updaed!")
	
	@name.getter
	def name(self):
		print("name is :", self.__name)		
				
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
