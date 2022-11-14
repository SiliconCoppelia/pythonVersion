import Aesthetics as aest
from enum import Enum
import pandas as pd


import random as rand
from random import randrange
# Import Classes
from relevance import *
from valence import *
from useIntention import *

sentNeg: str = r"./sentences/affordance/Affordance/AffordanceNegstream"
sentPos: str = r"./sentences/affordance/Affordance/AffordancePosstream"

suffixNeg: list = ['AffordanceNegObser', 'AffordanceNegAss', 'Relevance', 'Valence', 'UI', 'Involvement', 'Distance', 'DissimilarityInUI', 'DissimilarityInInvolvement', 'DissimilarityInDistance']
suffixPos: list = ['AffordancePosObser', 'AffordancePos', 'Relevance', 'Valence', 'UI', 'Involvement', 'Distance', 'SimilarityInUI', 'SimilarityInInvolvement', 'SimilarityInDistance']

class FileEngine:

    def ExcelreturnSent(self) -> tuple:
        negative: pd.DataFrame = pd.read_excel(sentNeg + ".xlsx")
        postive: pd.DataFrame = pd.read_excel(sentPos + ".xlsx")
        return (negative, postive)

    def TxtreturnSent(self) -> tuple:
        """pd.read_fwf(sentNeg)"""
        pos: list = [pd.read_csv(sentPos + "/" + path + ".txt", header=None, sep='/') for path in suffixPos]
        neg: list = [pd.read_csv(sentNeg + "/" + path + ".txt", header=None, sep='/') for path in suffixNeg]
        pos = pd.concat(pos, axis=1)
        pos.columns = pos.iloc[0]
        pos = pos[1:]
        neg = pd.concat(neg, axis=1)
        neg.columns = neg.iloc[0]
        neg = neg[1:]
        return (neg, pos)


class StayWith(Enum):
    SKILLFUL: tuple = [5, [num / 100 for num in range(67, 100, 1)]]
    BRILLIANT: tuple = [4, [num / 100 for num in range(34, 67, 1)]]
    NORMAL: tuple = [3, [num / 100 for num in range(0, 34, 1)]]
    UNFAMILIAR: list = [2, [(-1)*(num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(-1)*(num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [0, [(-1)*(num / 100) for num in range(67, 100, 1)]]


class Affordance:



    # Dependency Dimensions Declaration
    relevance = Relevance()
    valence = Valence()
    useIntention = UseIntention()


    def setAffordance(self, affordance):
        self.affordance = affordance

    inputIn: float
    appear: tuple
    sentences: tuple

    def __init__(self, outerln: float) -> None:
        self.inputIn = outerln
        self.sentences = FileEngine().ExcelreturnSent()
        return

    def undefined(self) -> None:
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    def getAffor(self) -> str:
        self.undefined()
        print("Hey there! you will receive a pandas dataframe! which type is a pandas.Series."
              "Here is its column name, you can get wanted sentence buy calling it.\n" +
              " ".join(self.sentences[0].columns.to_list()) + "\n" +
              " ".join(self.sentences[1].columns.tolist())+ "\n\n")
        if self.appear[0] < 3:
            return self.sentences[0].iloc[self.appear[0]]
        elif self.appear[0] > 3:
            return self.sentences[1].iloc[self.appear[0] - 3]


    def affordanceModeling(self, posOrNeg):
        self.relevance.setInputFactor("affordance")
        self.valence.setInputFactor("affordance")
        self.useIntention.setInputFactor("affordance")

        self.relevance.setRelevance()


