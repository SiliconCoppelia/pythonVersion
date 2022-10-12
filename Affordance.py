import Aesthetics as aest
from enum import Enum
import pandas as pd

sentNeg: str = r"/sentences/affordance/Affordance/AffordanceNegstream.xlsx"
sentPos: str = r"/sentences/affordance/Affordance/AffordancePosstream.xlsx"


class FileEngine:

    def returnSent(self) -> tuple:
        negative: pd.DataFrame = pd.read_excel(sentNeg)
        postive: pd.DataFrame = pd.read_excel(sentPos)
        return (negative, postive)


class StayWith(Enum):
    SKILLFUL: tuple = [5, [num / 100 for num in range(83, 100, 1)]]
    BRILLIANT: tuple = [4, [num / 100 for num in range(67, 83, 1)]]
    NORMAL: tuple = [3, [num / 100 for num in range(50, 67, 1)]]
    UNFAMILIAR: list = [2, [num / 100 for num in range(33, 50, 1)]]
    AWKWARD: list = [1, [num / 100 for num in range(17, 33, 1)]]
    UNSKILLFUL: list = [0, [num / 100 for num in range(0, 17, 1)]]


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
        self.sentences = FileEngine().returnSent()
        return

    def undefined(self) -> None:
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    def getAffor(self) -> tuple:
        self.undefined()
        if self.appear[1] < 3: return self.sentences[0]
        return tuple([self.appear[1], self.inputIn])
