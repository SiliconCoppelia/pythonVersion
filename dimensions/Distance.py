import pandas as pd
import random as rand
from enum import Enum


class FileRead:

    def __init__(self) -> None:
        self.invpreffix: str = r"../sentences/distance/"
        self.negsuffix: list = ["aff_neg/_low", "aff_neg/_mid", "aff_neg/_high"]
        self.posuffix: list = ["aff_pos/_low", "aff_pos/_mid", "aff_pos/_high"]

    def generator(self) -> tuple:
        negcolumns = [open(self.invpreffix + file + ".txt", "r").readlines() for file in
                      self.negsuffix]
        poscolumns = [open(self.invpreffix + file + ".txt", "r").readlines() for file in
                      self.posuffix]
        return negcolumns, poscolumns


class StayWith(Enum):
    UNFAMILIAR: list = [0, [(num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [2, [(num / 100) for num in range(67, 100, 1)]]


class Distance:

    def __init__(self, val: float, attitude: str):
        self.val = val
        self.neg, self.pos = FileRead().generator()
        self.alt = attitude
        self.negPanel: list = [len(num) - 1 for num in self.neg]
        self.posPanel: list = [len(num) - 1 for num in self.pos]

    def identify(self):
        temp: float = float("{:.2f}".format(self.val))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.val = iterator.value
                break

    def returnPivot(self, side: int, pos: int):
        if side:
            if not self.posPanel[pos]: self.posPanel[pos] = len(self.pos[pos])
            sentence = self.pos[pos][rand.randint(0, self.posPanel[pos])]
            self.posPanel[pos] -= 1
            return sentence
        else:
            if not self.negPanel[pos]: self.negPanel[pos] = len(self.neg[pos])
            sentence = self.neg[pos][rand.randint(0, self.negPanel[pos])]
            self.negPanel[pos] -= 1
            return sentence

    def DistanceNeg(self):
        """
        remember convert self.val from float into int
        """
        return self.returnPivot(0, self.val[0])

    def DistancePos(self):
        return self.returnPivot(1, self.val[0])

    def setDistance(self, val: int):
        self.val = val

    def returnDist(self):
        self.identify()
        if self.alt.lower() == "neg":
            return self.DistanceNeg()
        else:
            return self.DistancePos()


if __name__ == "__main__":
    jack = Distance(0.8, "pos")
    print(jack.returnDist())
