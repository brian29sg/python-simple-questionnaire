from Display import displayInfo
import os

''' 

The function executeSurvey prompts the user to enter their name and age, which will then 
be passed on to the function displayInfo to determine the nature of the user.
 
A 'try' method is used to ensure the age entered is a number.
 
'''

def executeSurvey():
	
	while raw_input("\nPlease type 'e' and press 'enter' to exit. \nOtherwise type any other letter to continue: ") != "e":
		
		print "\n" * 100
		name = raw_input("Please enter your name: ")
		
		while True:
			try:
				age = int(raw_input("\nPlease enter your age: "))
		
			except ValueError:
				print "\nPlease enter your age again. "
			
			else:
				displayInfo(name, age)
				break
		


