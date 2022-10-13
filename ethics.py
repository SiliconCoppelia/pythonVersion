# Import libraries
"""
	For random draw in the pool of corpus
	Reference of random int inclusive:
	https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
"""
from random import randrange
# Import Classes
from relevance import *
from valence import *
from useIntention import *

"""
LINES_OF_POS_LOW_SCORE_OBSERVATION = 16
LINES_OF_POS_MID_SCORE_OBSERVSTION = 23
LINES_OF_POS_HIGH_SCORE_OBSERVATION = 22
TOTAL_LINES_OF_POS_OBSERVATION = LINES_OF_POS_LOW_SCORE_OBSERVATION + LINES_OF_POS_MID_SCORE_OBSERVSTION + LINES_OF_POS_HIGH_SCORE_OBSERVATION

LINES_OF_POS_LOW_SCORE_ASSESSMENT = 17
LINES_OF_POS_MID_SCORE_ASSESSMENT = 15
LINES_OF_POS_HIGH_SCORE_ASSESSMENT = 25
TOTAL_LINES_OF_POS_ASSESSMENT = LINES_OF_POS_LOW_SCORE_ASSESSMENT + LINES_OF_POS_MID_SCORE_ASSESSMENT + LINES_OF_POS_HIGH_SCORE_ASSESSMENT
"""

class Ethics():

	"""
		Reference of initializing multiple list: 
		https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
	"""
	pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))

	def __init__(self, score, relevance, valence):
		self.score = score
		self.relevance = relevance
		self.valence = valence

	def getEthRel(self):
		return Relevance(self.relevance, "ethics")

	def getEthVal(self):
		return Valence(self.valence, "ethics")

	def getEthUseInten(self):
		return UseIntention()

	"""
	def loadCorpus(self):
		self.pos_obs_low = open("./sentences/ethics/eth_pos_low.txt", "r").readlines()
		self.pos_obs_mid = open("./sentences/ethics/eth_pos_mid.txt", "r").readlines()
		self.pos_obs_high = open("./sentences/ethics/eth_pos_high.txt", "r").readlines()
		self.pos_asses_low = open("./sentences/ethics/eth_pos_asses_low.txt", "r").readlines()
		self.pos_asses_mid = open("./sentences/ethics/eth_pos_asses_mid.txt", "r").readlines()
		self.pos_asses_high = open("./sentences/ethics/eth_pos_asses_high.txt", "r").readlines()
	"""

	def getEthObservation(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.pos_obs_low) == 0: 
			self.pos_obs_low = open("./sentences/ethics/eth_pos_low.txt", "r").readlines()
		if len(self.pos_obs_mid) == 0:
			self.pos_obs_mid = open("./sentences/ethics/eth_pos_mid.txt", "r").readlines()
		if len(self.pos_obs_high) == 0:
			self.pos_obs_high = open("./sentences/ethics/eth_pos_high.txt", "r").readlines()

		# Get Observation
		if self.score < 0.34:
			return self.pos_obs_low.pop(randrange(len(self.pos_obs_low))).replace("\n", "")
		elif self.score >= 0.34 and self.score < 0.67:
			return self.pos_obs_mid.pop(randrange(len(self.pos_obs_mid))).replace("\n", "")
		else:
			return self.pos_obs_high.pop(randrange(len(self.pos_obs_high))).replace("\n", "")

	def getEthAssessment(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.pos_asses_low) == 0:
			self.pos_asses_low = open("./sentences/ethics/eth_pos_asses_low.txt", "r").readlines()
		if len(self.pos_asses_mid) == 0:
			self.pos_asses_mid = open("./sentences/ethics/eth_pos_asses_mid.txt", "r").readlines()
		if len(self.pos_asses_high) == 0:
			self.pos_asses_high = open("./sentences/ethics/eth_pos_asses_high.txt", "r").readlines()

		# Get Assessment
		if self.score < 0.34:
			return self.pos_asses_low.pop(randrange(len(self.pos_asses_low))).replace("\n", "")
		elif self.score >= 0.34 and self.score < 0.67:
			return self.pos_asses_mid.pop(randrange(len(self.pos_asses_mid))).replace("\n", "")
		else:
			return self.pos_asses_high.pop(randrange(len(self.pos_asses_high))).replace("\n", "")

	"""
		Reference of replacing escape characters in string:
		https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
	"""


"""
eth = Ethics(0.5, 0.5)
#eth.loadCorpus()
print(eth.getEthObservation(0))
print(eth.getEthAssessment(0))

print(eth.getEthObservation(0.32))
print(eth.getEthAssessment(0.32))

print(eth.getEthObservation(0.532))
print(eth.getEthAssessment(0.532))

print(eth.getEthObservation(0.89))
print(eth.getEthAssessment(0.89))
"""


"""
	Ethics Object update log:
		v 1.1 created on 4th Oct
		v 1.2 created on 13th Oct
			- Seperation of Positive sentences into different files
			- Finalize Ethics Positive model
"""



