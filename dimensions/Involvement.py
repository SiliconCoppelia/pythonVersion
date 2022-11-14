from enum import Enum
import Aesthetics as aest
import Affordance as affor


class Engagement:
    variable: dict

    def __init__(self, variable: dict):
        self.variable = variable
        return

    def callOfValue(self):
        self.variable["aest"] = aest.Aesthetics(self.variable["Aesthetics"]).getAest()
        self.variable["affor"] = affor.Affordance(self.variable["Affordance"]).getAffor()
        self.variable["epis"]: int
        self.variable["relevance"]: int
        self.variable["valence"]: int

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

    class Distance:
        entrance: dict
        localVar: dict

        def __init__(self, outer):
            self.entrance = outer
            return

        def weight(self):
            ...
