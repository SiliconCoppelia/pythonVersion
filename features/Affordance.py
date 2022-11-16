import sys

sys.path.append("..")

from dimensions.valence import *
from dimensions.relevance import *
from dimensions.useIntention import *
from dimensions.Similarity import *


class Affordance:
    """
	Reference of initializing multiple list:
	https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
    """

    relevance = Relevance()
    valence = Valence()
    useIntention = UseIntention()
    similarity = Similarity()
    # disSimilarity = Dissimilarity()
    # involvement = Involvement()
    # disatance = Distance()

    pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))
    neg_obs_low, neg_obs_mid, neg_obs_high, neg_asses_low, neg_asses_mid, neg_asses_high = ([] for i in range(6))

    def __init__(self):
        self.affordance = 0

    def setAffordance(self, affordance):
        self.affordance = affordance

    # -----------------------------POSITIVE-----------------------------#

    def getPosAffObservation(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.pos_obs_low) == 0:
            self.pos_obs_low = open("./sentences/affordance/aff_pos_obs_low.txt", "r").readlines()
        if len(self.pos_obs_mid) == 0:
            self.pos_obs_mid = open("./sentences/affordance/aff_pos_obs_mid.txt", "r").readlines()
        if len(self.pos_obs_high) == 0:
            self.pos_obs_high = open("./sentences/affordance/aff_pos_obs_high.txt", "r").readlines()

        # Get Observation
        if self.affordance < 0.34:
            return self.pos_obs_low.pop(randrange(len(self.pos_obs_low))).replace("\n", "")
        elif self.affordance >= 0.34 and self.affordance < 0.67:
            return self.pos_obs_mid.pop(randrange(len(self.pos_obs_mid))).replace("\n", "")
        else:
            return self.pos_obs_high.pop(randrange(len(self.pos_obs_high))).replace("\n", "")

    def getPosAffAssessment(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.pos_asses_low) == 0:
            self.pos_asses_low = open("./sentences/affordance/aff_pos_ass_low.txt", "r").readlines()
        if len(self.pos_asses_mid) == 0:
            self.pos_asses_mid = open("./sentences/affordance/aff_pos_ass_mid.txt", "r").readlines()
        if len(self.pos_asses_high) == 0:
            self.pos_asses_high = open("./sentences/affordance/aff_pos_ass_high.txt", "r").readlines()

        # Get Assessment
        if self.affordance < 0.34:
            return self.pos_asses_low.pop(randrange(len(self.pos_asses_low))).replace("\n", "")
        elif self.affordance >= 0.34 and self.affordance < 0.67:
            return self.pos_asses_mid.pop(randrange(len(self.pos_asses_mid))).replace("\n", "")
        else:
            return self.pos_asses_high.pop(randrange(len(self.pos_asses_high))).replace("\n", "")

    # -----------------------------NEGATIVE-----------------------------#

    def getNegAffObservation(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.neg_obs_low) == 0:
            self.neg_obs_low = open("./sentences/affordance/aff_neg_obs_low.txt", "r").readlines()
        if len(self.neg_obs_mid) == 0:
            self.neg_obs_mid = open("./sentences/affordance/eth_neg_obs_mid.txt", "r").readlines()
        if len(self.neg_obs_high) == 0:
            self.neg_obs_high = open("./sentences/affordance/eth_neg_obs_high.txt", "r").readlines()

        # Get Observation
        if self.affordance < 0.34:
            return self.neg_obs_low.pop(randrange(len(self.neg_obs_low))).replace("\n", "")
        elif self.affordance >= 0.34 and self.affordance < 0.67:
            return self.neg_obs_mid.pop(randrange(len(self.neg_obs_mid))).replace("\n", "")
        else:
            return self.neg_obs_high.pop(randrange(len(self.neg_obs_high))).replace("\n", "")

    def getNegAffAssessment(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.neg_asses_low) == 0:
            self.neg_asses_low = open("./sentences/affordance/aff_neg_ass_low.txt", "r").readlines()
        if len(self.neg_asses_mid) == 0:
            self.neg_asses_mid = open("./sentences/affordance/aff_neg_ass_mid.txt", "r").readlines()
        if len(self.neg_asses_high) == 0:
            self.neg_asses_high = open("./sentences/affordance/aff_neg_ass_high.txt", "r").readlines()

        # Get Assessment
        if self.affordance < 0.34:
            return self.neg_asses_low.pop(randrange(len(self.neg_asses_low))).replace("\n", "")
        elif self.affordance >= 0.34 and self.affordance < 0.67:
            return self.neg_asses_mid.pop(randrange(len(self.neg_asses_mid))).replace("\n", "")
        else:
            return self.neg_asses_high.pop(randrange(len(self.neg_asses_high))).replace("\n", "")

    """
		Reference of replacing escape characters in string:
		https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
	"""


if __name__ == "__main__":
    jack = Affordance()
    jack.setAffordance(0.35)
    # print(jack.getNegAffAssessment())
    print(jack.getPosAffAssessment())
