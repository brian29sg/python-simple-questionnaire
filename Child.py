import sys
from familyMember import familyMember

class Child(familyMember):

	def __init__(self, name, age, education, allowance):
		self.name = name
		self.age = age
		self.education = education
		self.allowance = allowance
	
	def getEducation(self):
		return self.education
	
	def getAllowance(self):
		return self.allowance

