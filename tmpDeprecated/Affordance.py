import Aesthetics as aest
from enum import Enum
import pandas as pd
import numpy as np
import random as rand

from dimensions import valence as vale
from dimensions import relevance as reval
from dimensions import useIntention as ui

initial: str = r"../sentences/affordance/"

sentNeg: str = "aff_neg"
sentPos: str = "aff_pos"

suffix = ["_ass", "_obs", ["_low", "_mid", "_high"]]

__Total_file: int = 11


class FileEngine:

    def ExcelreturnSent(self) -> tuple:
        negative: pd.DataFrame = pd.read_excel(initial + "Affordance/AffordanceNegstream.xlsx", header=True)
        positive: pd.DataFrame = pd.read_excel(initial + "Affordance/AffordancePosstream.xlsx", header=True)
        return (negative, positive)

    def TxtreturnSent(self) -> tuple:
        """pd.read_fwf(sentNeg)"""
        pos: list = [pd.read_csv(initial + sentPos + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2]
                     for rank in suffix[2]]
        neg: list = [pd.read_csv(initial + sentNeg + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2]
                     for rank in suffix[2]]
        # pos: pd.DataFrame = pd.concat(pos, axis=1)
        # pos.columns = [*["afforObs" + nuts for nuts in suffix[2]], *["afforAss" + nuts for nuts in suffix[2]]]
        # neg = pd.concat(neg, axis=1)
        # neg.columns = [*["afforObs" + nuts for nuts in suffix[2]], *["afforAss" + nuts for nuts in suffix[2]]]
        return (neg, pos)


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

    def __init__(self, outerln: float) -> None:
        self.inputIn = outerln
        self.sentences = FileEngine().TxtreturnSent()
        self.panel: list = [len(self.sentences[0][num]) for num in range(0, len(self.sentences[0]))] + \
                           [len(self.sentences[1][num]) for num in range(0, len(self.sentences[1]))]
        self.relevance = reval.Relevance()
        self.valence = vale.Valence()
        self.useIntention = ui.UseIntention()
        return

    def panelPivot(self, sequence: int, pivot: int) -> int:
        pointer: int = sequence + pivot * 6
        if not self.panel[pointer]: self.panel[pointer] = [num for num in range(0, len(self.sentences[0]))]
        randnum = np.random.randint(self.panel[pointer], size=1)
        self.panel[pointer] -= 1
        return randnum[0]

    def undefined(self) -> None:
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    """
    be remind here the getAffor would return a python dataframe to caller
    """

    def negSpeaker(self) -> None:
        print(self.sentences[0][self.appear[0]].iloc[self.panelPivot(self.appear[0], 0)].to_string(header=False, index=False))
        print(self.sentences[0][self.appear[0] + 3].iloc[self.panelPivot(self.appear[0] + 3, 0)].to_string(header=False, index=False))
        # print(self.relevance.getNegRelevance())
        # print(self.valence.getNegValence())
        # print(self.useIntention.getNegUI())

    def posSpeaker(self) -> None:
        print(self.sentences[1][self.appear[0] - 3].iloc[self.panelPivot(self.appear[0] - 3, 1)].to_string(header=False, index=False))
        print(self.sentences[1][self.appear[0]].iloc[self.panelPivot(self.appear[0], 1)].to_string(header=False, index=False))
        # print(self.relevance.getPosRelevance())
        # print(self.valence.getPosValence())
        # print(self.useIntention.getPosUI())

    def affordanceModeling(self) -> None:
        self.relevance.setInputFactor("affordance")
        self.valence.setInputFactor("affordance")
        self.useIntention.setInputFactor("affordance")

        "Oops, due to operation roles are differnet with previous one, the initialization"

        if self.inputIn > 0.66:
            self.valence.setValence(rand.uniform(0.67, 1))
            self.useIntention.setUseIntention(rand.uniform(0.67, 1))
        elif 0.66 >= self.inputIn > 0.33:
            self.valence.setValence(rand.uniform(0.34, 0.67))
            self.useIntention.setUseIntention(rand.uniform(0.34, 0.67))
        else:
            self.valence.setValence(rand.uniform(0, 0.33))
            self.useIntention.setUseIntention(rand.uniform(0, 0.33))

    def coppeliaSpeaksEthics(self) -> None:
        self.undefined()
        self.affordanceModeling()
        if self.appear[0] < 3:
            self.negSpeaker()
        else:
            self.posSpeaker()


if __name__ == "__main__":
    jack = Affordance(0.9)
    jack.coppeliaSpeaksEthics()
