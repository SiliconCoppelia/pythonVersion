"""
	__init__ Class
	Current Dimensions: Ethics, Affordances, and Aesthetics
	Current Settings of Coppeélia: 
			1. Coppélia prefers good-looking subjects
			2. Coppélia prefers kind and friendly subjects
			3. Coppélia wishes to make friends or date with agents
			4. Coppélia is an individual with kind and friendly personality, and a smart subject
	To-Do: 
			1. Formulation of The Order Of Saying Things In Ethics
			2. ....
"""

# Import Dependencies
# https://stackoverflow.com/questions/43023970/builtin-function-or-method-object-has-no-attribute-randrange
import random as rand
# Import Classes
from ethics import *
from Affordance import *


class Coppelia():

	ethics = Ethics()
	# affordance = Affordance()

	greetings = "Hi, I'm Coppélia."
	goal = "I want to be friends with you"

	def __init__(self):
		print(self.greetings)

	def setEthics(self, score):
		self.ethics.setEthics(score)

	def coppeliaSpeaksEthics(self, posOrNeg):
		self.ethics.coppeliaSpeaksEthics(posOrNeg)

	# Reference of random fractions between two values: 
	# https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

coppelia = Coppelia()
coppelia.setEthics(rand.uniform(0, 1))
coppelia.coppeliaSpeaksEthics("positive")
coppelia.coppeliaSpeaksEthics("negative")