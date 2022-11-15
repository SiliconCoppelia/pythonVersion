from enum import Enum
import Aesthetics as aest
import Affordance as affor
import valence as vals
import relevance as rel
import pandas as pd
class FileRead:

    def __init__(self) -> None:
        self.invpreffix: str = r"/sentences/Involvement/"
        self.invsuffix: list = ["Inv_neg_low", "Inv_neg_mid", "Inv_neg_high",
                                "Inv_pos_low", "Inv_pos_mid", "Inv_pos_high"]

    def generator(self) -> tuple:
        negcolumns = [pd.read_csv(self.invpreffix + file + ".txt", header=file) for file in self.invsuffix[0:3]]
        poscolumns = [pd.read_csv(self.invpreffix + file + ".txt", header=file) for file in self.invsuffix[3:6]]
        return (pd.concat(negcolumns), pd.concat(poscolumns))

class Engagement:
    variable: dict

    def __init__(self, variable: dict):
        self.variable = variable
        return

    def callOfValue(self):
        self.variable["aest"] = aest.Aesthetics(self.variable["Aesthetics"]).getAest()
        self.variable["affor"] = affor.Affordance(self.variable["Affordance"]).getAffor()
        self.variable["epis"]: int
        self.variable["relevance"]: int = rel.Relevance().getNegRelevance() if self.variable["rel"] < 0 else rel.Relevance().getPosRelevance()
        self.variable["valence"]: int = vals.Valence().getNegValence() if self.variable["vals"] < 0 else vals.Valence().getPosValence()

    class Involvement:
        entrance: dict
        localGet: dict
        """
        entrance :var indicates the needed input stored
        in dict, which contains the initial value of 
        Aesthetics, Affordances, and Epistemic 
        :parameter: outer will be an instance of outer class
        """

        def __init__(self, outer):
            self.entrance = outer.variable
            return

        def weight(self):
            ...

        def getInvolvement(self) -> None:
            res = FileRead().generator()
            if self.entrance["inv"] > 0 and self.entrance["inv"] < 0.34: return res[1]["Inv_pos_low"]
            elif self.entrance["inv"] > 0.34 and self.entrance["inv"] < 0.67: return res[1]["Inv_pos_mid"]
            elif self.entrance["inv"] > 0.67 and self.entrance["inv"] < 1: return res[1]["Inv_pos_high"]


    class Distance:
        entrance: dict
        localVar: dict

        def __init__(self, outer):
            self.entrance = outer
            return

        def weight(self):
            ...
