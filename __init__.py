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
	affordance = Affordance()

	greetings = "Hi, I'm Coppélia."
	goal = "I want to be friends with you"

	def __init__(self):
		print(self.greetings)

	def setEthics(self, score):
		self.ethics.setEthics(score)

	def ethicsModeling(self):
		self.ethics.__class__.relevance.setRelevance(rand.uniform(0.67, 1))
		self.ethics.__class__.relevance.setInputFactor("ethics")
		self.ethics.__class__.valence.setInputFactor("ethics")
		self.ethics.__class__.useIntention.setInputFactor("ethics")

		if self.ethics.getEthics() > 0.66:
			self.ethics.__class__.valence.setValence(rand.uniform(0.67, 1))
			self.ethics.__class__.useIntention.setUseIntention(rand.uniform(0.67, 1))
		elif self.ethics.getEthics() <= 0.66 and self.ethics.getEthics() > 0.33:
			self.ethics.__class__.valence.setValence(rand.uniform(0.34, 0.67))
			self.ethics.__class__.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
		else:
			self.ethics.__class__.valence.setValence(rand.uniform(0, 0.33))
			self.ethics.__class__.useIntention.setUseIntention(rand.uniform(0, 0.33))

	def speaksEthic(self):
		self.ethicsModeling()
		print(self.goal)
		print(self.ethics.getPosEthObservation())
		print(self.ethics.getPosEthAssessment())
		print(self.ethics.__class__.relevance.getRelevance())
		print(self.ethics.__class__.valence.getValence())
		print(self.ethics.__class__.useIntention.getUseIntention())

	# Reference of random fractions between two values: 
	# https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

coppelia = Coppelia()
coppelia.setEthics(rand.uniform(0, 1))
coppelia.speaksEthic()

# #Variable declaration
# greetings = "Hi, I'm Coppélia."
# goal = "I want to be friends with you"

# print(greetings + "\n" + goal)
# ethics = Ethics()

# #---------------POSITIVE---------------#

# ethics.setEthics(rand.uniform(0, 1))
# print(ethics.getPosEthObservation())
# print(ethics.getPosEthAssessment())

# ethics.__class__.relevance.setRelevance(rand.uniform(0.67, 1))
# ethics.__class__.relevance.setInputFactor("ethics")
# ethics.__class__.valence.setInputFactor("ethics")

# if ethics.getEthics() > 0.66:
# 	ethics.__class__.valence.setValence(rand.uniform(0.67, 1))
# elif ethics.getEthics() <= 0.66 and ethics.getEthics() > 0.33:
# 	ethics.__class__.valence.setValence(rand.uniform(0.34, 0.67))
# else:
# 	ethics.__class__.valence.setValence(rand.uniform(0, 0.33))

# print(ethics.__class__.relevance.getrelevance())
# print(ethics.__class__.valence.getvalence())