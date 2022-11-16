# Import libraries
"""
	For random draw in the pool of corpus
	Reference of random int inclusive:
	https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
"""
import random as rand
from random import randrange

# Import Classes
import sys
sys.path.append('..')
from dimensions.relevance import *
from dimensions.valence import *
from dimensions.useIntention import *
from dimensions.Involvement import *
from dimensions.Distance import *
from dimensions.Similarity import *
from dimensions.Dissimilarity import *

class Ethics():

	"""
		Reference of initializing multiple list: 
		https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
	"""

	relevance = Relevance()
	valence = Valence()
	useIntention = UseIntention()
	similarity = Similarity()
	disSimilarity = Dissimilarity()
	involvement = Involvement()
	distance = Distance()

	pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))
	neg_obs_low, neg_obs_mid, neg_obs_high, neg_asses_low, neg_asses_mid, neg_asses_high = ([] for i in range(6))

	def setEthics(self, ethics):
		self.ethics = ethics


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


	def ethicsModeling(self, posOrNeg):

		self.relevance.setInputFactor("ethics")
		self.valence.setInputFactor("ethics")
		self.useIntention.setInputFactor("ethics")

		self.relevance.setRelevance(rand.uniform(0.67, 1))
		# self.similarity.setSimilarity(0.2, 0.32, rand.uniform(0.67, 1), rand.uniform(0.67, 1))

		if self.ethics > 0.66:
			self.valence.setValence(rand.uniform(0.67, 1))
			self.useIntention.setUseIntention(rand.uniform(0.67, 1))
		elif self.ethics <= 0.66 and self.ethics > 0.33:
			self.valence.setValence(rand.uniform(0.34, 0.67))
			self.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
		else:
			self.valence.setValence(rand.uniform(0, 0.33))
			self.useIntention.setUseIntention(rand.uniform(0, 0.33))


		if(posOrNeg == "positive"):
			if self.ethics > 0.66:
				self.involvement.setInvolvement(rand.uniform(0.67, 1))
			elif self.ethics <= 0.66 and self.ethics > 0.33:
				self.involvement.setInvolvement(rand.uniform(0.34, 0.67))
			else:
				self.involvement.setInvolvement(rand.uniform(0, 0.34))
			self.distance.setDistance(rand.uniform(0, 0.5))
			# self.similarity.setSimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(), self.involvement.getInvolvement(), self.distance.getDistance())


		elif(posOrNeg == "negative"):
			if self.ethics > 0.66:
				self.distance.setDistance(rand.uniform(0.67, 1))
			elif self.ethics <= 0.66 and self.ethics > 0.33:
				self.distance.setDistance(rand.uniform(0.34, 0.67))
			else:
				self.distance.setDistance(rand.uniform(0, 0.34))
			self.involvement.setInvolvement(rand.uniform(0, 0.5))
			# self.disSimilarity.setDissimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(), self.involvement.getInvolvement(), self.distance.getDistance())


	def coppeliaSpeaksEthics(self, posOrNeg):
		self.ethicsModeling(posOrNeg)
		
		if(posOrNeg == "positive"):
			self.response = [self.getPosEthObservation(), self.getPosEthAssessment(), self.relevance.getPosRelevance(),\
				self.valence.getPosValence(), self.useIntention.getPosUI()]
			# print(self.similarity.getSimilarityOnUI())
			# print(self.similarity.getSimilarityOnInv())
			# print(self.similarity.getSimilarityOnDis())
		else:
			self.response = [self.getNegEthObservation(), self.getNegEthAssessment(), self.relevance.getNegRelevance(),\
				self.valence.getNegValence(), self.useIntention.getNegUI()]
		# print(self.involvement.getInvolvement())
		# print(self.distance.getDistance())

		print("\n".join(self.response))


