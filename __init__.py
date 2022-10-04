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

# Import libraries
from random import random
# Import Dependencies
from ethics import *
#from relevance import *
#from valence import *
#from useIntention import *


class Coppelia(Ethics):

	#Variable declaration
	greetings = "Hi, I'm Coppélia."
	ethicsResponse = []

	def greet(self):
		print(greetings)

	def speaks(self, dimension, score):
		# ...

# Coppélia object initilaization
coppélia = Coppelia()
# Ethics object initialization
ethics = Ethics(random())


coppélia.greet()