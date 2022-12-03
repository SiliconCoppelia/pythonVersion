from random import randrange
import pandas as pd
import relevance
import valence
from Similarity import Similarity as simi

class Factors:
    def __init__(self, relevance, valence, similarity: float, affordance: float = 0, w_rel_val: float = 0.5) -> None:
        self.affordance = affordance
        self.relevance = relevance
        self.valence = valence
        self.similarity = similarity
        self.W_R_val = w_rel_val

    def Str_valence_relevance(self):
        return

    def Str_process(self):
        return

    def matrix_algorithm(self, args: float, coeff_x: float = 1, b: float = 0):
        """
        algorithm temporarily set as linear function: y = coeff_x * args + b
        """
        return coeff_x * args + b

    def relevance_merge_valence(self):
        self.rev_val: pd.DataFrame = pd.DataFrame({"rel": self.relevance, "val": self.valence})
        self.rev_val.apply(self.matrix_algorithm, args=(0.476, -0.014, ))
        return self.rev_val.dot(pd.DataFrame({"weight": [self.W_R_val, 1-self.W_R_val]}))

    def similarity_to_involvement(self):
        return self.relevance_merge_valence() * self.similarity

    def affordance_to_involvement(self, involvement, neg: float = 0.3, pos: float = 0.1):
        if self.affordance < 0.5: return involvement - neg * self.affordance
        return involvement + pos * self.affordance

    def Int_valence_relevance(self):
        if not self.affordance: return self.similarity_to_involvement()
        return self.affordance_to_involvement(0.3)


class Involvement:
    # aff_low, aff_mid, aff_high, eth_low, eth_mid, eth_high = ([] for i in range(6))
    invl_high, invl_low, invl_mid = ([] for i in range(3))

    rel = relevance.Relevance().getPosRelevance()
    val = valence.Valence().getPosValence()
    similarity = simi()

    def __init__(self):
        self.factor = Factors(relevance=self.rel, valence=self.val, similarity=self.similarity.getSimilarityOnInv())

    def setInvl(self, involvement):
        self.involvement = involvement

    def getInvl(self):
        return self.involvement

    # def setInputFactor(self, input_factor):
    #     self.input_factor = input_factor

    # def select_factor_dic(self):
    #     if self.input_factor == "involvement":
    #         return "Inv"
    #     elif self.input_factor == "ethics":
    #         return "eth"
    #     else:
    #         pass
    #         # return "aest_pos/"

    def getInvolvement(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.invl_low) == 0:
            self.invl_low = open("./sentences/involvement/invl_low.txt", "rb").readlines()
        if len(self.invl_mid) == 0:
            self.invl_mid = open("./sentences/involvement/invl_mid.txt", "rb").readlines()
        if len(self.invl_high) == 0:
            self.invl_high = open("./sentences/involvement/invl_high.txt", "rb").readlines()

        if self.involvement < 0.34:
            return (self.invl_low.pop(randrange(len(self.invl_low))).decode("utf-8")).replace("\n", "")
        elif self.involvement < 0.67:
            return (self.invl_mid.pop(randrange(len(self.invl_mid))).decode("utf-8")).replace("\n", "")
        else:
            return (self.invl_high.pop(randrange(len(self.invl_high))).decode("utf-8")).replace("\n", "")

    def getEthics(self):
        return self.factor.relevance_merge_valence()

    def Involvement2Simi(self):
        res = self.factor.similarity_to_involvement()
        self.similarity.similarity = res
        return self.similarity.getSimilarityOnInv()

    def Involvement_Bias_Affordance(self):
        self.setInvl(self.factor.affordance_to_involvement(self.involvement))
        return self.getInvolvement()

# if __name__ == "__main__":
#     jack = Involvement()
#     jack.setInputFactor("involvement")
#     jack.setInvolvement(0.6)
#     print(jack.getInvolvement())
