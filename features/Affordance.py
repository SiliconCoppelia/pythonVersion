from enum import Enum
import pandas as pd
import numpy as np
import random as rand
import sys
sys.path.append("..")

from dimensions.valence import *
from dimensions.relevance import *
from dimensions.useIntention import *

initial: str = r"../sentences/affordance/"

sentNeg: str = "aff_neg"
sentPos: str = "aff_pos"

suffix = ["_ass", "_obs", ["_low", "_mid", "_high"]]

__Total_file: int = 11


class FileEngine:

    # def ExcelreturnSent(self) -> tuple:
    #     negative: pd.DataFrame = pd.read_excel(initial + "Affordance/AffordanceNegstream.xlsx", header=True)
    #     positive: pd.DataFrame = pd.read_excel(initial + "Affordance/AffordancePosstream.xlsx", header=True)
    #     return negative, positive

    def TxtreturnSent(self) -> tuple:
        """pd.read_fwf(sentNeg)"""
        pos: list = [pd.read_csv(initial + sentPos + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2]
                     for rank in suffix[2]]
        neg: list = [pd.read_csv(initial + sentNeg + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2]
                     for rank in suffix[2]]
        return neg, pos


class StayWith(Enum):
    SKILLFUL: tuple = [5, [num / 100 for num in range(67, 100, 1)]]
    BRILLIANT: tuple = [4, [num / 100 for num in range(34, 67, 1)]]
    NORMAL: tuple = [3, [num / 100 for num in range(0, 34, 1)]]
    UNFAMILIAR: list = [0, [(-1) * (num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(-1) * (num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [2, [(-1) * (num / 100) for num in range(67, 100, 1)]]


class Affordance:
    """
    version 1.0
    generally the same logistic process with the Aesthetics
    """

    inputIn: float
    appear: tuple
    sentences: tuple

    def __init__(self, outerln: float, attitude: str) -> None:
        self.inputIn = outerln
        self.sentences = FileEngine().TxtreturnSent()
        self.panel: list = [len(self.sentences[0][num]) for num in range(0, len(self.sentences[0]))] + \
                           [len(self.sentences[1][num]) for num in range(0, len(self.sentences[1]))]
        self.attitude = attitude.lower()
        self.relevance = Relevance()
        self.valence = Valence()
        self.useIntention = UseIntention()
        return

    def panelPivot(self, sequence: int, pivot: int) -> int:
        pointer: int = sequence + pivot * 6
        if not self.panel[pointer]: self.panel[pointer] = len(self.sentences[pivot][sequence])
        randnum = np.random.randint(self.panel[pointer], size=1)
        self.panel[pointer] -= 1
        return randnum[0]

    def undefined(self) -> None:
        """
        undefined is used to detect the emotion of Coppelia. to decide further reaction to
        the target. So this function must be called before modeling
        """
        if self.attitude in ["neg", "negative"]: self.inputIn *= -1
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    def negSpeaker(self) -> tuple:
        """
        neg_ass, neg_obs are both string sentence
        """
        neg_ass = self.sentences[0][self.appear[0]].iloc[self.panelPivot(self.appear[0], 0)].to_string(header=False, index=False)
        neg_obs = self.sentences[0][self.appear[0] + 3].iloc[self.panelPivot(self.appear[0] + 3, 0)].to_string(header=False, index=False)
        return neg_ass, neg_obs
        # print(self.relevance.getNegRelevance())
        # print(self.valence.getNegValence())
        # print(self.useIntention.getNegUI())

    def posSpeaker(self) -> tuple:
        """
        pos_ass and pos_obs are both a string sentence, not anything else
        """
        pos_ass = self.sentences[1][self.appear[0] - 3].iloc[self.panelPivot(self.appear[0] - 3, 1)].to_string(header=False, index=False)
        pos_obs = self.sentences[1][self.appear[0]].iloc[self.panelPivot(self.appear[0], 1)].to_string(header=False, index=False)
        return pos_ass, pos_obs
        # print(self.relevance.getPosRelevance())
        # print(self.valence.getPosValence())
        # print(self.useIntention.getPosUI())

    # def affordanceModeling(self) -> None:
    #     self.relevance.setInputFactor("affordance")
    #     self.valence.setInputFactor("affordance")
    #     self.useIntention.setInputFactor("affordance")
    #
    #     if self.inputIn > 0.66:
    #         self.valence.setValence(rand.uniform(0.67, 1))
    #         self.useIntention.setUseIntention(rand.uniform(0.67, 1))
    #     elif 0.66 >= self.inputIn > 0.33:
    #         self.valence.setValence(rand.uniform(0.34, 0.67))
    #         self.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
    #     else:
    #         self.valence.setValence(rand.uniform(0, 0.33))
    #         self.useIntention.setUseIntention(rand.uniform(0, 0.33))
    #
    # def coppeliaSpeaksEthics(self) -> None:
    #     self.undefined()
    #     self.affordanceModeling()
    #     if self.appear[0] < 3:
    #         self.negSpeaker()
    #     else:
    #         self.posSpeaker()


if __name__ == "__main__":
    # Example 1:
    jack = Affordance(0.9, "neg")
    jack.undefined()
    print(jack.negSpeaker()[0], jack.negSpeaker()[1])
    print(jack.posSpeaker()[0], jack.posSpeaker()[1])

    # Example 2:
    bob = Affordance(0.3, "pos")
    jack.undefined()
    print(jack.negSpeaker()[0], jack.negSpeaker()[1])
    print(jack.posSpeaker()[0], jack.posSpeaker()[1])

    # you can only invoke function negSpeaker and posSpeaker to access what Coppelia
    # would speak. I've commented the modeling and other word expression function