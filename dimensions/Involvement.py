import pandas as pd
import random as rand
from enum import Enum


class FileRead:

    def __init__(self) -> None:
        self.invpreffix: str = r"../sentences/Involvement/"
        self.invsuffix: list = ["Inv_neg_low", "Inv_neg_mid", "Inv_neg_high",
                                "Inv_pos_low", "Inv_pos_mid", "Inv_pos_high"]

    def generator(self) -> tuple:
        negcolumns = [pd.read_csv(self.invpreffix + file + ".txt", header=file) for file in self.invsuffix[0:3]]
        poscolumns = [pd.read_csv(self.invpreffix + file + ".txt", header=file) for file in self.invsuffix[3:6]]
        return negcolumns, poscolumns


class StayWith(Enum):
    UNFAMILIAR: list = [0, [(num / 100) for num in range(0, 34, 1)]]
    AWKWARD: list = [1, [(num / 100) for num in range(34, 67, 1)]]
    UNSKILLFUL: list = [2, [(num / 100) for num in range(67, 100, 1)]]


class Involvement:

    def __init__(self, val: int, attitude: str):
        self.val = val
        self.neg, self.pos = FileRead().generator()
        self.alt = attitude

    def panel(self) -> None:
        self.negPanel: list = [len(num) for num in self.neg]
        self.posPanel: list = [len(num) for num in self.pos]

    def returnPivot(self, side: int, pos: int):
        if side:
            if not self.posPanel[pos]: self.posPanel[pos] = len(self.pos[pos])
            self.posPanel[pos] -= 1
            return self.pos[rand.randint(0, self.posPanel[pos])]
        else:
            if not self.negPanel[pos]: self.negPanel[pos] = len(self.neg[pos])
            self.negPanel[pos] -= 1
            return self.neg[rand.randint(0, self.negPanel[pos])]

    def InvolvementNeg(self):
        """
        remember convert self.val from float into int
        """
        return self.neg[self.val][self.returnPivot(0, self.val)]

    def InvolvementPos(self):
        return self.pos[self.val][self.returnPivot(0, self.val)]

    def setInvolvement(self, val: int):
        self.val = val

    def identify(self):
        temp: float = float("{:.2f}".format(self.val))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.val = iterator.value
                break

    def returnInvol(self, attitude: str):
        self.identify()
        if attitude.lower() == "neg":
            return self.InvolvementNeg()
        else:
            return self.InvolvementPos()
