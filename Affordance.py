import Aesthetics as aest
from enum import Enum
import pandas as pd

sentNeg: str = r"./sentences/affordance/Affordance/AffordanceNegstream."
sentPos: str = r"./sentences/affordance/Affordance/AffordancePosstream."


class FileEngine:

    def ExcelreturnSent(self) -> tuple:
        negative: pd.DataFrame = pd.read_excel(sentNeg + "xlsx")
        postive: pd.DataFrame = pd.read_excel(sentPos + "xlsx")
        return (negative, postive)

    def TxtreturnSent(self) -> pd.DataFrame:
        """pd.read_fwf(sentNeg)"""
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
                self.appear = iterator.value()
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
    jack = Affordance(0.87)
    print(jack.getAffor())

def tempSpliter():
    file: pd.DataFrame = pd.read_excel(r"D:\Code Working Area\Python\SiliconCoppelia\pythonVersion\sentences\affordance\Affordance\AffordanceNegstream.xlsx")
    for name, val in file.iteritems():
        pd.to_csv(r"./sentences/affordance/Affordance/AffordanceNeg/" + name + ".txt")
