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
import random as rand
# Import Classes
from ethics import *


class Coppelia():

	#Variable declaration
	greetings = "Hi, I'm Coppélia."
	goal = "I want to be friends with you"

	def greet(self):
		print(self.greetings)
		print(self.goal)

	def getEthicsSentences(self, score):

		# Reference of random fractions between two values: 
		# https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range
		if score > 0.66:
			eth = Ethics(score, rand.uniform(0.67, 1), rand.uniform(0.67, 1))
		elif score <= 0.66 and score > 0.33:
			eth = Ethics(score, rand.uniform(0.67, 1), rand.uniform(0.34, 0.67))
		else:
			eth = Ethics(score, rand.uniform(0.67, 1), rand.uniform(0, 0.33))
		return eth

# Coppélia object initilaization
coppelia = Coppelia()
coppelia.greet()

eth = coppelia.getEthicsSentences(rand.uniform(0, 1))
eth_rel = eth.getEthRel()
eth_val = eth.getEthVal()
eth_rel.loadCorpus()
eth_val.loadCorpus()
print(eth.getEthObservation())
print(eth.getEthAssessment())
print(eth_rel.getrelevance())
print(eth_val.getvalence())


"""
rel = Relevance(0.7389, "ethics")
rel.loadCorpus()
print(rel.getrelevance())
"""