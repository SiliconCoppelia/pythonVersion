import random
import enum
from abs import ABCMeta, abstractmethod
import numpy as np

import sys
sys.path.append("..")
from dimensions.relevance import *
from dimensions.valence import *
from dimensions.useIntention import *
from dimensions.Involvement import *
from dimensions.Distance import *
from dimensions.Similarity import *
from dimensions.Dissimilarity import *

class Question:
    Physics: str = "Are you good at badminton?"
    Mental: str = "lets play a mind teaser! shall we?"
    Reality: str = "A old woman need help because she lost her way, will you help her?"

    Reject: list = []
    Accept: list = []

    class Type(enum):
        OBSTACLE = False
        AID = True

    def ask_question(self, question: str):
        print(question)
        res = input()
        if res in self.Reject: return self.Type.OBSTACLE
        elif res in self.Accept: return self.Type.AID
        else: raise Exception("User input invalid word.")


class Affordance_Counterpart(Question):
    def __init__(self):
        super().__init__()
        self.STABLE = 0.5
        self.Device = self.Type.AID

    respon_platform: dict = {}

    def response(self):
        self.respon_platform[self.Physics] = (self.ask_question(self.Physics), )
        self.respon_platform[self.Mental] = (self.ask_question(self.Mental), )
        self.respon_platform[self.Reality] = (self.ask_question(self.Reality), )

    @abstractmethod
    def Device_working(self): pass

    def Device_camera(self):
        res = self.Device_working()
        if type(res) is bool: return res
        raise Exception("Cant identify camera working situation...")

    def physics_judge(self):
        self.Device_camera()
        if self.respon_platform[self.Physics][0]:
            if not self.Device: self.respon_platform[self.Physics][1] = self.STABLE
            self.respon_platform[self.Physics][1] = [random.uniform(0.3, 0.7), random.uniform(0, 0.3)]
        else: self.respon_platform[self.Physics][1] = [random.uniform(0.0, 0.3), random.uniform(0.3, 0.7)]

    def mental_judge(self):
        if self.respon_platform[self.Mental][0]:
            self.respon_platform[self.Mental][1] = [random.uniform(0.5, 0.8), random.uniform(0.1, 0.5)]
        else: self.respon_platform[self.Mental][1] = [random.uniform(0.1, 0.5), random.uniform(0.1, 0.5)]

    def reality_judge(self):
        pass

    def divide_judgement(self):
        self.physics_judge()
        self.mental_judge()
        self.reality_judge()

    def return_value(self):
        physics, mental = np.array(self.respon_platform[self.Physics][1]), np.array(self.respon_platform[self.Mental][1]).T
        result = np.multiply(physics, mental)
        return {"Negaff": result[0], "Posaff": result[1]}



# class Affordance:
#     """
#         Reference of initializing multiple list:
#         https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
#     """
#
#     relevance = Relevance()
#     valence = Valence()
#     useIntention = UseIntention()
#     similarity = Similarity()
#     disSimilarity = Dissimilarity()
#     involvement = Involvement()
#     distance = Distance()
#
#     pos_obs_low, pos_obs_mid, pos_obs_high, pos_asses_low, pos_asses_mid, pos_asses_high = ([] for i in range(6))
#     neg_obs_low, neg_obs_mid, neg_obs_high, neg_asses_low, neg_asses_mid, neg_asses_high = ([] for i in range(6))
#
#     posOrder = ["[Computer Vision]", "[Affor Encoding]", "[Goal Statement]", "[Relevance]", "[Valence]", "[Use Itention]", \
#                     "[Similarity on UI]", "[Involvement]", "[Similarity on Invl]", "[Distance]", "[Similarity on Dist]", ""]
#
#     negOrder = ["[Computer Vision]", "[Affor Encoding]", "[Goal Statement]", "[Relevance]", "[Valence]", "[Use Itention]", \
#                     "[DisSimilarity on UI]", "[Involvement]", "[DisSimilarity on Invl]", "[Distance]", "[DisSimilarity on Dist]", ""]
#
#     def __init__(self):
#         self.affordance = 0
#
#     def setAffordance(self, affordance):
#         self.affordance = affordance
#
#     def setGoal(self, goal):
#         self.goal = goal
#
#     # -----------------------------POSITIVE-----------------------------#
#
#     def getPosAffObservation(self):
#         # Load corpus if all variants in one dimension are used up
#         if len(self.pos_obs_low) == 0:
#             self.pos_obs_low = open("./sentences/affordance/aff_pos_obs_low.txt", "r").readlines()
#         if len(self.pos_obs_mid) == 0:
#             self.pos_obs_mid = open("./sentences/affordance/aff_pos_obs_mid.txt", "r").readlines()
#         if len(self.pos_obs_high) == 0:
#             self.pos_obs_high = open("./sentences/affordance/aff_pos_obs_high.txt", "r").readlines()
#
#         # Get Observation
#         if self.affordance < 0.34:
#             return self.pos_obs_low.pop(randrange(len(self.pos_obs_low))).replace("\n", "")
#         elif self.affordance >= 0.34 and self.affordance < 0.67:
#             return self.pos_obs_mid.pop(randrange(len(self.pos_obs_mid))).replace("\n", "")
#         else:
#             return self.pos_obs_high.pop(randrange(len(self.pos_obs_high))).replace("\n", "")
#
#     def getPosAffAssessment(self):
#         # Load corpus if all variants in one dimension are used up
#         if len(self.pos_asses_low) == 0:
#             self.pos_asses_low = open("./sentences/affordance/aff_pos_ass_low.txt", "r").readlines()
#         if len(self.pos_asses_mid) == 0:
#             self.pos_asses_mid = open("./sentences/affordance/aff_pos_ass_mid.txt", "r").readlines()
#         if len(self.pos_asses_high) == 0:
#             self.pos_asses_high = open("./sentences/affordance/aff_pos_ass_high.txt", "r").readlines()
#
#         # Get Assessment
#         if self.affordance < 0.34:
#             return self.pos_asses_low.pop(randrange(len(self.pos_asses_low))).replace("\n", "")
#         elif self.affordance >= 0.34 and self.affordance < 0.67:
#             return self.pos_asses_mid.pop(randrange(len(self.pos_asses_mid))).replace("\n", "")
#         else:
#             return self.pos_asses_high.pop(randrange(len(self.pos_asses_high))).replace("\n", "")
#
#     # -----------------------------NEGATIVE-----------------------------#
#
#     def getNegAffObservation(self):
#         # Load corpus if all variants in one dimension are used up
#         if len(self.neg_obs_low) == 0:
#             self.neg_obs_low = open("./sentences/affordance/aff_neg_obs_low.txt", "r").readlines()
#         if len(self.neg_obs_mid) == 0:
#             self.neg_obs_mid = open("./sentences/affordance/aff_neg_obs_mid.txt", "r").readlines()
#         if len(self.neg_obs_high) == 0:
#             self.neg_obs_high = open("./sentences/affordance/aff_neg_obs_high.txt", "r").readlines()
#
#         # Get Observation
#         if self.affordance < 0.34:
#             return self.neg_obs_low.pop(randrange(len(self.neg_obs_low))).replace("\n", "")
#         elif self.affordance >= 0.34 and self.affordance < 0.67:
#             return self.neg_obs_mid.pop(randrange(len(self.neg_obs_mid))).replace("\n", "")
#         else:
#             return self.neg_obs_high.pop(randrange(len(self.neg_obs_high))).replace("\n", "")
#
#     def getNegAffAssessment(self):
#         # Load corpus if all variants in one dimension are used up
#         if len(self.neg_asses_low) == 0:
#             self.neg_asses_low = open("./sentences/affordance/aff_neg_ass_low.txt", "r").readlines()
#         if len(self.neg_asses_mid) == 0:
#             self.neg_asses_mid = open("./sentences/affordance/aff_neg_ass_mid.txt", "r").readlines()
#         if len(self.neg_asses_high) == 0:
#             self.neg_asses_high = open("./sentences/affordance/aff_neg_ass_high.txt", "r").readlines()
#
#         # Get Assessment
#         if self.affordance < 0.34:
#             return self.neg_asses_low.pop(randrange(len(self.neg_asses_low))).replace("\n", "")
#         elif self.affordance >= 0.34 and self.affordance < 0.67:
#             return self.neg_asses_mid.pop(randrange(len(self.neg_asses_mid))).replace("\n", "")
#         else:
#             return self.neg_asses_high.pop(randrange(len(self.neg_asses_high))).replace("\n", "")
#
#     """
#         Reference of replacing escape characters in string:
#         https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
#     """
#
#     def affordanceModeling(self, posOrNeg):
#
#         self.relevance.setInputFactor("affordance")
#         self.valence.setInputFactor("affordance")
#         self.useIntention.setInputFactor("affordance")
#
#         self.relevance.setRelevance(rand.uniform(0.67, 1))
#         # self.similarity.setSimilarity(0.2, 0.32, rand.uniform(0.67, 1), rand.uniform(0.67, 1))
#
#         if self.affordance > 0.66:
#             self.valence.setValence(rand.uniform(0.67, 1))
#             self.useIntention.setUseIntention(rand.uniform(0.67, 1))
#         elif self.affordance <= 0.66 and self.affordance > 0.33:
#             self.valence.setValence(rand.uniform(0.34, 0.67))
#             self.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
#         else:
#             self.valence.setValence(rand.uniform(0, 0.33))
#             self.useIntention.setUseIntention(rand.uniform(0, 0.33))
#
#
#         if(posOrNeg == "positive"):
#             if self.affordance > 0.66:
#                 self.involvement.setInvl(rand.uniform(0.67, 1))
#             elif self.affordance <= 0.66 and self.affordance > 0.33:
#                 self.involvement.setInvl(rand.uniform(0.34, 0.67))
#             else:
#                 self.involvement.setInvl(rand.uniform(0, 0.34))
#             self.distance.setDist(rand.uniform(0, 0.5))
#             self.similarity.setSimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(), self.involvement.getInvl(), self.distance.getDist())
#
#
#         elif(posOrNeg == "negative"):
#             if self.affordance > 0.66:
#                 self.distance.setDist(rand.uniform(0.67, 1))
#             elif self.affordance <= 0.66 and self.affordance > 0.33:
#                 self.distance.setDist(rand.uniform(0.34, 0.67))
#             else:
#                 self.distance.setDist(rand.uniform(0, 0.34))
#             self.involvement.setInvl(rand.uniform(0, 0.5))
#             self.disSimilarity.setDissimilarity(rand.uniform(0, 1), self.useIntention.getUseIntention(), self.involvement.getInvl(), self.distance.getDist())
#
#
#     def coppeliaSpeaksAffordance(self, posOrNeg):
#         self.affordanceModeling(posOrNeg)
#
#         if(posOrNeg == "positive"):
#             self.response = [self.getPosAffObservation(), self.getPosAffAssessment(), self.goal, self.relevance.getPosRelevance(),\
#                 self.valence.getPosValence(), self.useIntention.getPosUI(), self.similarity.getSimilarityOnUI(), \
#                 self.involvement.getInvolvement(), self.similarity.getSimilarityOnInv(), self.distance.getDistance(), self.similarity.getSimilarityOnDis()]
#         else:
#             self.response = [self.getNegAffObservation(), self.getNegAffAssessment(), self.goal, self.relevance.getNegRelevance(),\
#                 self.valence.getNegValence(), self.useIntention.getNegUI(), self.disSimilarity.getDissimilarityOnUI(), \
#                 self.involvement.getInvolvement(), self.disSimilarity.getDissimilarityOnInv(), self.distance.getDistance(), self.disSimilarity.getDissimilarityOnDis()]
#
#         # print("\n".join(self.response))
#         self.response.append("\n")
#         # Reference:
#         # https://towardsdatascience.com/formatting-strings-and-numbers-in-python-16a326a5d5b3#:~:text=Aligning%20the%20output%20neatly%20using,that%20you%20want%20to%20format.&text=We%20can%20use%20the%20fortmat,in%20the%20order%20we%20want.
#         for i in range(0, len(self.response)):
#             if posOrNeg == "positive":
#                 print(f"{self.posOrder[i]:>25}{self.response[i]:>120}")
#             else:
#                 print(f"{self.negOrder[i]:>25}{self.response[i]:>120}")
#

# if __name__ == "__main__":
#     jack = Affordance()
#     jack.setAffordance(0.35)
#     # print(jack.getNegAffAssessment())
#     print(jack.getPosAffAssessment())
