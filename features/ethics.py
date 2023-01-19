# Import libraries
"""
	For random draw in the pool of corpus
	Reference of random int inclusive:
	https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
"""
import random as rand
from random import randrange

# Import Classes
#Import Coppeélia Profile

class Ethics():

	"""
		Reference of initializing multiple list: 
		https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
	"""

	pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))
	neg_obs_low, neg_obs_mid, neg_obs_high, neg_asses_low, neg_asses_mid, neg_asses_high = ([] for i in range(6))

	posOrder = ["[Goal Statement]", "[Computer Vision]", "[Ethics Encoding]", "[Relevance]", "[Valence]", "[Use Itention]", \
					"[Similarity on UI]", "[Involvement]", "[Similarity on Invl]", "[Distance]", "[Similarity on Dist]", ""]

	negOrder = ["[Goal Statement]", "[Computer Vision]", "[Ethics Encoding]", "[Relevance]", "[Valence]", "[Use Itention]", \
					"[DisSimilarity on UI]", "[Involvement]", "[DisSimilarity on Invl]", "[Distance]", "[DisSimilarity on Dist]", ""]

	# coppeliaProfile = CoppeliaProfile()
	"""
		If the 
	"""

	def setEthics(self, ethics):
		self.ethics = ethics

	def setGoal(self, goal):
		self.goal = goal

	#-----------------------------POSITIVE-----------------------------#

	def getPosEthObservation(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.pos_obs_low) == 0: 
			self.pos_obs_low = open("./sentences/ethics/eth_pos_low.txt", "r").readlines()
		if len(self.pos_obs_mid) == 0:
			self.pos_obs_mid = open("./sentences/ethics/eth_pos_mid.txt", "r").readlines()
		if len(self.pos_obs_high) == 0:
			self.pos_obs_high = open("./sentences/ethics/eth_pos_high.txt", "r").readlines()

		# Get Observation
		if self.ethics < 0.34:
			return self.pos_obs_low.pop(randrange(len(self.pos_obs_low))).replace("\n", "")
		elif self.ethics >= 0.34 and self.ethics < 0.67:
			return self.pos_obs_mid.pop(randrange(len(self.pos_obs_mid))).replace("\n", "")
		else:
			return self.pos_obs_high.pop(randrange(len(self.pos_obs_high))).replace("\n", "")

	def getPosEthAssessment(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.pos_asses_low) == 0:
			self.pos_asses_low = open("./sentences/ethics/eth_pos_asses_low.txt", "r").readlines()
		if len(self.pos_asses_mid) == 0:
			self.pos_asses_mid = open("./sentences/ethics/eth_pos_asses_mid.txt", "r").readlines()
		if len(self.pos_asses_high) == 0:
			self.pos_asses_high = open("./sentences/ethics/eth_pos_asses_high.txt", "r").readlines()

		# Get Assessment
		if self.ethics < 0.34:
			return self.pos_asses_low.pop(randrange(len(self.pos_asses_low))).replace("\n", "")
		elif self.ethics >= 0.34 and self.ethics < 0.67:
			return self.pos_asses_mid.pop(randrange(len(self.pos_asses_mid))).replace("\n", "")
		else:
			return self.pos_asses_high.pop(randrange(len(self.pos_asses_high))).replace("\n", "")

	#-----------------------------NEGATIVE-----------------------------#

	def getNegEthObservation(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.neg_obs_low) == 0: 
			self.neg_obs_low = open("./sentences/ethics/eth_neg_low.txt", "r").readlines()
		if len(self.neg_obs_mid) == 0:
			self.neg_obs_mid = open("./sentences/ethics/eth_neg_mid.txt", "r").readlines()
		if len(self.neg_obs_high) == 0:
			self.neg_obs_high = open("./sentences/ethics/eth_neg_high.txt", "r").readlines()

		# Get Observation
		if self.ethics < 0.34:
			return self.neg_obs_low.pop(randrange(len(self.neg_obs_low))).replace("\n", "")
		elif self.ethics >= 0.34 and self.ethics < 0.67:
			return self.neg_obs_mid.pop(randrange(len(self.neg_obs_mid))).replace("\n", "")
		else:
			return self.neg_obs_high.pop(randrange(len(self.neg_obs_high))).replace("\n", "")

	def getNegEthAssessment(self):
		# Load corpus if all variants in one dimension are used up
		if len(self.neg_asses_low) == 0:
			self.neg_asses_low = open("./sentences/ethics/eth_neg_asses_low.txt", "r").readlines()
		if len(self.neg_asses_mid) == 0:
			self.neg_asses_mid = open("./sentences/ethics/eth_neg_asses_mid.txt", "r").readlines()
		if len(self.neg_asses_high) == 0:
			self.neg_asses_high = open("./sentences/ethics/eth_neg_asses_high.txt", "r").readlines()

		# Get Assessment
		if self.ethics < 0.34:
			return self.neg_asses_low.pop(randrange(len(self.neg_asses_low))).replace("\n", "")
		elif self.ethics >= 0.34 and self.ethics < 0.67:
			return self.neg_asses_mid.pop(randrange(len(self.neg_asses_mid))).replace("\n", "")
		else:
			return self.neg_asses_high.pop(randrange(len(self.neg_asses_high))).replace("\n", "")

	"""
		Reference of replacing escape characters in string:
		https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
	"""