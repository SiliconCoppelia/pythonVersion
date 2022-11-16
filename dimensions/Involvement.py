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

from random import randrange
import sys
# sys.path.append("..")

class Involvement:
    # involvement = 0
    # input_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high = ([] for i in range(6))

    def setInvolvement(self, involvement):
        self.involvement = involvement

    def getInvolvement(self):
        return self.involvement

    # def setInputFactor(self, input_factor):
    #     self.input_factor = input_factor

    # def select_factor_dic(self):
    #     if (self.input_factor == "involvement negative"):
    #         return "inv_neg"
    #     elif (self.input_factor == "involvement positive"):
    #         return "inv_pos"
    #     else:
    #         pass
    #         # return "aest_pos/"

    def getPosInvolvement(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.p_low) == 0:
            self.p_low = open("sentences/involvement/" + self.select_factor_dic() + "_low.txt", "rb").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/involvement/" + self.select_factor_dic() + "_mid.txt", "rb").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/involvement/" + self.select_factor_dic() + "_high.txt", "rb").readlines()

        if self.involvement < 0.34:
            return self.p_low.pop(randrange(len(self.p_low))).decode("utf-8")
        elif self.involvement < 0.67:
            return self.p_mid.pop(randrange(len(self.p_mid))).decode("utf-8")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).decode("utf-8")

    def getNegInvolvement(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.n_low) == 0:
            self.n_low = open("sentences/involvement/" + self.select_factor_dic() + "_low.txt", "r").readlines()
        if len(self.n_mid) == 0:
            self.n_mid = open("sentences/involvement/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
        if len(self.n_high) == 0:
            self.n_high = open("sentences/involvement/" + self.select_factor_dic() + "_high.txt", "r").readlines()

        if self.involvement < 0.34:
            return self.n_high.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.involvement < 0.67:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        else:
            return self.n_low.pop(randrange(len(self.n_high))).replace("\n", "")

if __name__ == "__main__":
    jack = Involvement()
    jack.setInputFactor("involvement negative")
    jack.setRelevance(0.6)
    print(jack.getPosInvolvement())
