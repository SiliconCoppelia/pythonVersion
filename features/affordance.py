import numpy as np
import sys
import random as rand
from abcmeta import ABC, abstractmethod

sys.path.append("..")
from dimensions.relevance import *
from dimensions.valence import *
from dimensions.useIntention import *
from dimensions.Involvement import *
from dimensions.Distance import *
# from dimensions.Dissimilarity import *
from dimensions.Dissimilarity import *


class Upper_calss_interface(ABC):
    @abstractmethod
    def Aff_data(self, data: dict):
        pass


# in this class, the data input will assume as json file according to
# this address: https://bitbucket.org/robopop/silicon-coppelia/src/master/data/input.json
class Affordance_approximate(Upper_calss_interface):
    aff_input: dict

    def __init__(self) -> None:
        """
        suppose to serialize some data structure here
        """
        ...

    def define_input(self, val: dict):
        self.aff_input = val

    def feature_split(self):
        aff_on_features: dict = UpperClass()
        ...

    def value_compute(self, ):
        """
        it is believed that this function more like a interface that only responsible for
        data transformation among various part
        """

        ...

    def semantic_output(self, ):
        ...

    def return_Value(self):
        if not self.aff_input: Exception("Value Error, input is empty.")
        return self.aff_input

    def temporary_framework_call(self, aff_val: float):
        aff_object: Affordance = Affordance()
        aff_object.setAffordance(aff_val)
        return aff_object


class Affordance:
    """
        Reference of initializing multiple list:
        https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
    """

    relevance = Relevance()
    valence = Valence()
    useIntention = UseIntention()
    # similarity = Similarity()
    disSimilarity = Dissimilarity()
    involvement = Involvement()
    distance = Distance()

    pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))
    neg_obs_low, neg_obs_mid, neg_obs_high, neg_asses_low, neg_asses_mid, neg_asses_high = ([] for i in range(6))

    posOrder = ["[Computer Vision]", "[Affor Encoding]", "[Goal Statement]", "[Relevance]", "[Valence]",
                "[Use Itention]", \
                "[Similarity on UI]", "[Involvement]", "[Similarity on Invl]", "[Distance]", "[Similarity on Dist]", ""]

    negOrder = ["[Computer Vision]", "[Affor Encoding]", "[Goal Statement]", "[Relevance]", "[Valence]",
                "[Use Itention]", \
                "[DisSimilarity on UI]", "[Involvement]", "[DisSimilarity on Invl]", "[Distance]",
                "[DisSimilarity on Dist]", ""]

    def __init__(self):
        self.affordance = 0

    def setAffordance(self, affordance):
        self.affordance = affordance

    def setGoal(self, goal):
        self.goal = goal

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
            self.neg_obs_mid = open("./sentences/affordance/aff_neg_obs_mid.txt", "r").readlines()
        if len(self.neg_obs_high) == 0:
            self.neg_obs_high = open("./sentences/affordance/aff_neg_obs_high.txt", "r").readlines()

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

    def affordanceModeling(self, posOrNeg):

        self.relevance.setInputFactor("affordance")
        self.valence.setInputFactor("affordance")
        self.useIntention.setInputFactor("affordance")

        self.relevance.setRelevance(rand.uniform(0.67, 1))
        # self.similarity.setSimilarity(0.2, 0.32, rand.uniform(0.67, 1), rand.uniform(0.67, 1))

        if self.affordance > 0.66:
            self.valence.setValence(rand.uniform(0.67, 1))
            self.useIntention.setUseIntention(rand.uniform(0.67, 1))
        elif self.affordance <= 0.66 and self.affordance > 0.33:
            self.valence.setValence(rand.uniform(0.34, 0.67))
            self.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
        else:
            self.valence.setValence(rand.uniform(0, 0.33))
            self.useIntention.setUseIntention(rand.uniform(0, 0.33))

        if (posOrNeg == "positive"):
            if self.affordance > 0.66:
                self.involvement.setInvl(rand.uniform(0.67, 1))
            elif self.affordance <= 0.66 and self.affordance > 0.33:
                self.involvement.setInvl(rand.uniform(0.34, 0.67))
            else:
                self.involvement.setInvl(rand.uniform(0, 0.34))
            self.distance.setDist(rand.uniform(0, 0.5))
            self.similarity.setSimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(),
                                          self.involvement.getInvl(), self.distance.getDist())


        elif (posOrNeg == "negative"):
            if self.affordance > 0.66:
                self.distance.setDist(rand.uniform(0.67, 1))
            elif self.affordance <= 0.66 and self.affordance > 0.33:
                self.distance.setDist(rand.uniform(0.34, 0.67))
            else:
                self.distance.setDist(rand.uniform(0, 0.34))
            self.involvement.setInvl(rand.uniform(0, 0.5))
            self.disSimilarity.setDissimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(),
                                                self.involvement.getInvl(), self.distance.getDist())

    def coppeliaSpeaksAffordance(self, posOrNeg):
        self.affordanceModeling(posOrNeg)

        if (posOrNeg == "positive"):
            self.response = [self.getPosAffObservation(), self.getPosAffAssessment(), self.goal,
                             self.relevance.getPosRelevance(), 
                             self.valence.getPosValence(), self.useIntention.getPosUI(),
                             self.similarity.getSimilarityOnUI(),
                             self.involvement.getInvolvement(), self.similarity.getSimilarityOnInv(),
                             self.distance.getDistance(), self.similarity.getSimilarityOnDis()]
        else:
            self.response = [self.getNegAffObservation(), self.getNegAffAssessment(), self.goal,
                             self.relevance.getNegRelevance(),
                             self.valence.getNegValence(), self.useIntention.getNegUI(),
                             self.disSimilarity.getDissimilarityOnUI(),
                             self.involvement.getInvolvement(), self.disSimilarity.getDissimilarityOnInv(),
                             self.distance.getDistance(), self.disSimilarity.getDissimilarityOnDis()]

        # print("\n".join(self.response))
        self.response.append("\n")
        # Reference:
        # https://towardsdatascience.com/formatting-strings-and-numbers-in-python-16a326a5d5b3#:~:text=Aligning%20the%20output%20neatly%20using,that%20you%20want%20to%20format.&text=We%20can%20use%20the%20fortmat,in%20the%20order%20we%20want.
        for i in range(0, len(self.response)):
            if posOrNeg == "positive":
                print(f"{self.posOrder[i]:>25}{self.response[i]:>120}")
            else:
                print(f"{self.negOrder[i]:>25}{self.response[i]:>120}")


if __name__ == "__main__":
    jack = Affordance_approximate()
    test_jack = jack.temporary_framework_call(aff_val=0.35)
    print(test_jack.getPosAffAssessment())
    print(test_jack.getPosAffAssessment())
