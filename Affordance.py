import Aesthetics as aest
from enum import Enum
import pandas as pd

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
        self.sentences = FileEngine().TxtreturnSent()
        return

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
              " ".join(self.sentences[1].columns.tolist())+ "\n\n")
        if self.appear[0] < 3:
            return self.sentences[0].iloc[self.appear[0]]
        elif self.appear[0] > 3:
            return self.sentences[1].iloc[self.appear[0] - 3]

if __name__ == "__main__":
    jack = Affordance(0.35)
    print(jack.getAffor())

"""
alltheway: list = []
section: list = []
with open(sentNeg+"txt", "r") as fp:
    lines = fp.readline()
    for line in lines:
        if line.isspace():
            alltheway.append(section)
            section.clear()
        else: section.append(line)
return pd.DataFrame(alltheway)
"""