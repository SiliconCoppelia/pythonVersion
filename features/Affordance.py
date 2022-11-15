import Aesthetics as aest
from enum import Enum
import pandas as pd
import numpy as np

initial: str = r"./sentences/affordance/"

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
        pos: list = [pd.read_csv(initial + sentPos + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2] for rank in suffix[2]]
        neg: list = [pd.read_csv(initial + sentNeg + path + rank + ".txt", header=None, sep='/') for path in suffix[0:2] for rank in suffix[2]]
        pos: pd.DataFrame = pd.concat(pos, axis=1)
        pos.columns = [*["afforObs" + nuts for nuts in suffix[2]], *["afforAss" + nuts for nuts in suffix[2]]]
        neg = pd.concat(neg, axis=1)
        neg.columns = [*["afforObs" + nuts for nuts in suffix[2]], *["afforAss" + nuts for nuts in suffix[2]]]
        return (neg, pos)


class StayWith(Enum):
    SKILLFUL: tuple = [5, [num / 100 for num in range(67, 100, 1)]]
    BRILLIANT: tuple = [4, [num / 100 for num in range(34, 67, 1)]]
    NORMAL: tuple = [3, [num / 100 for num in range(0, 34, 1)]]
    UNFAMILIAR: list = [2, [(-1) * (num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(-1) * (num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [0, [(-1) * (num / 100) for num in range(67, 100, 1)]]


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
        self.panel: list = [len(self.sentences[0][num]) for num in self.sentences[0]] + \
            [len(self.sentences[1][num]) for num in self.sentences[1]]
        return

    def panelPivot(self, sequence: int, pivot: int) -> int:
        pointer: int =  sequence + pivot * 6
        if not self.panel[pointer]: self.panel[pointer] = [num for num in range(0, len(self.sentences[0]))]
        randnum = np.random.randint(self.panel[pointer], size=1)
        self.panel[pointer] -= 1
        return randnum

    def undefined(self) -> None:
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    """
    be remind here the getAffor would return a python dataframe to caller
    """

    def getAffor(self) -> str:
        self.undefined()
        print("Hey there! you will receive a pandas dataframe! which type is a pandas.Series."
              "Here is its column name, you can get wanted sentence buy calling it.\n" +
              " ".join(self.sentences[0].columns.to_list()) + "\n" +
              " ".join(self.sentences[1].columns.tolist()) + "\n\n")
        if self.appear[0] < 3:
            return self.sentences[0][[self.appear[0]]][self.panelPivot(self.appear[0], 0)]
        elif self.appear[0] > 3:
            return self.sentences[1][[self.appear[0] - 3]][self.panelPivot(self.appear[0], 1)]


if __name__ == "__main__":
    jack = Affordance(0.35)
    print(jack.getAffor())
