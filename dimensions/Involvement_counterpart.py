import pandas as pd
import random as rand
from enum import Enum


class FileRead:

    def __init__(self) -> None:
        self.invpreffix: str = r"../sentences/Involvement/"
        self.invsuffix: list = ["Inv_neg_low", "Inv_neg_mid", "Inv_neg_high",
                                "Inv_pos_low", "Inv_pos_mid", "Inv_pos_high"]

    def generator(self) -> tuple:
        negcolumns = [open(self.invpreffix + file + ".txt", "rb").readlines() for file in self.invsuffix[0:3]]
        poscolumns = [open(self.invpreffix + file + ".txt", "rb").readlines() for file in self.invsuffix[3:6]]
        return negcolumns, poscolumns


class StayWith(Enum):
    UNFAMILIAR: list = [0, [(num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [2, [(num / 100) for num in range(67, 100, 1)]]


class Involvement:

    def __init__(self, val: float, attitude: str):
        self.val = val
        self.neg, self.pos = FileRead().generator()
        self.alt = attitude
        self.negPanel: list = [len(num) -1 for num in self.neg]
        self.posPanel: list = [len(num) -1 for num in self.pos]


    def returnPivot(self, side: int, pos: int):
        if side:
            if not self.posPanel[pos]: self.posPanel[pos] = len(self.pos[pos])
            sentence = self.pos[pos][rand.randint(0, self.posPanel[pos])]
            self.posPanel[pos] -= 1
            return sentence.decode("utf-8")
        else:
            if not self.negPanel[pos]: self.negPanel[pos] = len(self.neg[pos])
            sentence = self.neg[pos][rand.randint(0, self.negPanel[pos])]
            self.negPanel[pos] -= 1
            return sentence.decode("utf-8")

    def InvolvementNeg(self):
        """
        remember convert self.val from float into int
        """
        return self.returnPivot(0, self.val[0])

    def InvolvementPos(self):
        return self.returnPivot(0, self.val[0])

    def setInvolvement(self, val: int):
        self.val = val

    def identify(self):
        temp: float = float("{:.2f}".format(self.val))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.val = iterator.value
                break

    def returnInvol(self):
        self.identify()
        if self.alt.lower() == "neg":
            return self.InvolvementNeg()
        else:
            return self.InvolvementPos()

if __name__ == "__main__":
    jack = Involvement(0.1, "neg")
    print(jack.returnInvol())