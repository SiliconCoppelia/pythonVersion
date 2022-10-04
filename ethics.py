# Import libraries
from random import random

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
	

	def __init__(self, ethics):
		self.ethics = ethics
		#print(len(self.corpus)) # 118

		global LINES_OF_POS_LOW_SCORE_OBSERVATION, LINES_OF_POS_MID_SCORE_OBSERVSTION, LINES_OF_POS_HIGH_SCORE_OBSERVATION
		global LINES_OF_POS_LOW_SCORE_ASSESSMENT, LINES_OF_POS_MID_SCORE_ASSESSMENT, LINES_OF_POS_HIGH_SCORE_ASSESSMENT
		observationLow = corpus.readlines()[0:LINES_OF_POS_LOW_SCORE_OBSERVATION]
		observationMid = corpus.readlines()[LINES_OF_POS_LOW_SCORE_OBSERVATION:LINES_OF_POS_MID_SCORE_OBSERVSTION]
		observationHigh = corpus.readlines()[LINES_OF_POS_MID_SCORE_OBSERVSTION:LINES_OF_POS_HIGH_SCORE_OBSERVATION]
		assessmentLow = corpus.readlines()[LINES_OF_POS_HIGH_SCORE_OBSERVATION:LINES_OF_POS_LOW_SCORE_ASSESSMENT]
		assessmentMid = corpus.readlines()[LINES_OF_POS_LOW_SCORE_ASSESSMENT:LINES_OF_POS_MID_SCORE_ASSESSMENT]
		assessmentHigh = corpus.readlines()[LINES_OF_POS_MID_SCORE_ASSESSMENT:LINES_OF_POS_HIGH_SCORE_ASSESSMENT]

	def getObservation(self):
		print(len(self.observationLow))
		print(len(self.observationMid))
		print(len(self.observationHigh))
		print(len(self.assessmentLow))
		print(len(self.assessmentMid))
		print(len(self.assessmentHigh))


eth = Ethics(random())
eth.getObservation()