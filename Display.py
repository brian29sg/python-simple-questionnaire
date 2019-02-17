from familyMember import familyMember 
from Adult import Adult
from Child import Child

'''

The function displayInfo sorts out whether the user is an adult or child
based on the age that was entered. Further prompts are issued to
summarise the user's details.

A 'try' method has been used when prompting the user for their 
allowance to ensure that what they have entered is valid.

When everything is valid, a new instance of 'Child' or 'Adult' is made. 

'''


def displayInfo(arg1, arg2):

	if arg2 <= 20:
		education = raw_input("\nPlease enter your education (eg. Year 10, College): ")

		while True:
			try:
				allowance = int(raw_input("\nPlease enter your weekly allowance (NZD$): "))
		
			except ValueError:
				print "\nPlease enter your allowance again. "
			
			else:
				member = Child(arg1, arg2, education, allowance)
				print member.getName() ,", aged", member.getAge(), "is in", member.getEducation(), "and gets $", member.getAllowance(), "weekly."
				break
			
		
	
	elif arg2 > 20:
		job = raw_input("\nPlease enter your job (eg. Engineer): ")

		while True:
			try:
				salary = int(raw_input("\nPlease enter your yearly salary (NZD$): "))
		
			except ValueError:
				print "\nPlease enter your salary again."
			
			else:
				member = Adult(arg1, arg2, job, salary)
				print "\n",member.getName() ,", aged", member.getAge(), "has a job as an", member.getJob(), "and earns $", member.getSalary(), "per annum."
				break
		
			
		
