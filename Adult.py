import sys
from familyMember import familyMember

class Adult(familyMember):

	def __init__(self, name, age, job, salary):
		self.name = name
		self.age = age
		self.job = job
		self.salary = salary
	
	def getJob(self):
		return self.job
	
	def getSalary(self):
		return self.salary


	
