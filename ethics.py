# Import libraries
# For random score of ethics
from random import random
"""
	For random draw in the pool of corpus
	Reference of random int inclusive:
	https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
"""
from random import randrange

LINES_OF_POS_LOW_SCORE_OBSERVATION = 16
LINES_OF_POS_MID_SCORE_OBSERVSTION = 23
LINES_OF_POS_HIGH_SCORE_OBSERVATION = 22
TOTAL_LINES_OF_POS_OBSERVATION = LINES_OF_POS_LOW_SCORE_OBSERVATION + LINES_OF_POS_MID_SCORE_OBSERVSTION + LINES_OF_POS_HIGH_SCORE_OBSERVATION

LINES_OF_POS_LOW_SCORE_ASSESSMENT = 17
LINES_OF_POS_MID_SCORE_ASSESSMENT = 15
LINES_OF_POS_HIGH_SCORE_ASSESSMENT = 25
TOTAL_LINES_OF_POS_ASSESSMENT = LINES_OF_POS_LOW_SCORE_ASSESSMENT + LINES_OF_POS_MID_SCORE_ASSESSMENT + LINES_OF_POS_HIGH_SCORE_ASSESSMENT

class Ethics:

	corpus = open("./ethicsPOS.txt", "r").readlines()
	"""
		Reference of initializing multiple list: 
		https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
	"""
	observationLow, observationMid, observationHigh, assessmentLow, assessmentMid, assessmentHigh = ([] for i in range(6))

	def loadCorpus(self):
		global LINES_OF_POS_LOW_SCORE_OBSERVATION, LINES_OF_POS_MID_SCORE_OBSERVSTION, LINES_OF_POS_HIGH_SCORE_OBSERVATION, TOTAL_LINES_OF_POS_OBSERVATION
		self.observationLow = self.corpus[0 : LINES_OF_POS_LOW_SCORE_OBSERVATION]
		self.observationMid = self.corpus[LINES_OF_POS_LOW_SCORE_OBSERVATION : LINES_OF_POS_LOW_SCORE_OBSERVATION + LINES_OF_POS_MID_SCORE_OBSERVSTION]
		self.observationHigh = self.corpus[LINES_OF_POS_MID_SCORE_OBSERVSTION : LINES_OF_POS_MID_SCORE_OBSERVSTION + LINES_OF_POS_HIGH_SCORE_OBSERVATION]

		global LINES_OF_POS_LOW_SCORE_ASSESSMENT, LINES_OF_POS_MID_SCORE_ASSESSMENT, LINES_OF_POS_HIGH_SCORE_ASSESSMENT, TOTAL_LINES_OF_POS_ASSESSMENT
		self.assessmentLow = self.corpus[TOTAL_LINES_OF_POS_OBSERVATION : TOTAL_LINES_OF_POS_OBSERVATION + LINES_OF_POS_LOW_SCORE_ASSESSMENT]
		self.assessmentMid = self.corpus[LINES_OF_POS_LOW_SCORE_ASSESSMENT : LINES_OF_POS_LOW_SCORE_ASSESSMENT + LINES_OF_POS_MID_SCORE_ASSESSMENT]
		self.assessmentHigh = self.corpus[LINES_OF_POS_MID_SCORE_ASSESSMENT : LINES_OF_POS_MID_SCORE_ASSESSMENT + LINES_OF_POS_HIGH_SCORE_ASSESSMENT]

	def getObservation(self, ethics):
		# Load corpus if all variants in one dimension are used up
		if len(self.observationLow) == 0 or len(self.observationMid) == 0 or len(self.observationHigh) == 0:
			self.loadCorpus()

		# Get Observation
		if ethics < 0.34:
			return self.observationLow.pop(randrange(len(self.observationLow))).replace("\n", "")
		elif ethics >= 0.34 and ethics < 0.67:
			return self.observationMid.pop(randrange(len(self.observationMid))).replace("\n", "")
		else:
			return self.observationHigh.pop(randrange(len(self.observationHigh))).replace("\n", "")

	def getAssessment(self, ethics):
		# Load corpus if all variants in one dimension are used up
		if len(self.assessmentLow) == 0 or len(self.assessmentMid) == 0 or len(self.assessmentHigh) == 0:
			self.loadCorpus()

		# Get Assessment
		if ethics < 0.34:
			return self.assessmentLow.pop(randrange(len(self.assessmentLow))).replace("\n", "")
		elif ethics >= 0.34 and ethics < 0.67:
			return self.assessmentMid.pop(randrange(len(self.assessmentMid))).replace("\n", "")
		else:
			return self.assessmentHigh.pop(randrange(len(self.assessmentHigh))).replace("\n", "")

	"""
		Reference of replacing escape characters in string:
		https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
	"""

eth = Ethics()
print(eth.getObservation(0))
print(eth.getAssessment(0))

print(eth.getObservation(0.32))
print(eth.getAssessment(0.32))

print(eth.getObservation(0.532))
print(eth.getAssessment(0.532))

print(eth.getObservation(0.89))
print(eth.getAssessment(0.89))



