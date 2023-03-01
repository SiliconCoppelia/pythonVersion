'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:

'''
from random import random
from random import randrange

class Relevance_Counterpart:

    def __init__(self):
        ...

    def extract_largest(self, mu1: set, mu2: set):
        """
        code this for fun
        """
        container=[_ for _ in range(0, 100)]


    def MI_or(self, mu1: set, mu2: set):
        """
        mamdani_implication, it is believed the contrast method need to overwrite
        """
        return max(mu1, mu2)

    def MI_and(self, mu1:set, mu2: set):
        return min(mu1, mu2)



class Relevance:

    relevance = 0
    input_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high = ([] for i in range(6))
    
    # def __init__(self, relevance, input_factor):
    #     self.relevance = relevance
    #     self.input_factor=input_factor

    def setRelevance(self, relevance):
        self.relevance = relevance

    def setInputFactor(self, input_factor):
        self.input_factor = input_factor
    
    def getRelValue(self):
        return self.relevance
    
    def select_factor_dic(self):
        if(self.input_factor=="ethics"): return "ethics/"
        elif(self.input_factor=="affordance"): return "affordance/"
        elif(self.input_factor=="aesthetics"): return "aesthetics/"
        else: return "epistemics/"

    def getPosRelevance(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/"+self.select_factor_dic()+"relevance/p_low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/"+self.select_factor_dic()+"relevance/p_mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/"+self.select_factor_dic()+"relevance/p_high.txt", "r").readlines()

        if self.relevance < 0.34:
            return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.relevance < 0.67:
            return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
    
    def getNegRelevance(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.n_low) == 0: 
            self.n_low = open("sentences/"+self.select_factor_dic()+"relevance/n_low.txt", "r").readlines()
        if len(self.n_mid) == 0:
            self.n_mid = open("sentences/"+self.select_factor_dic()+"relevance/n_mid.txt", "r").readlines()
        if len(self.n_high) == 0:
            self.n_high = open("sentences/"+self.select_factor_dic()+"relevance/n_high.txt", "r").readlines()

        if self.relevance < 0.34:
            return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.relevance < 0.67:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        else:
            return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")

    # def getRelevance(self):
    #     if len(self.p_low) == 0: 
    #         self.p_low = open("sentences/"+self.select_factor_dic()+"relevance/p_low.txt", "r").readlines()
    #     if len(self.p_mid) == 0:
    #         self.p_mid = open("sentences/"+self.select_factor_dic()+"relevance/p_mid.txt", "r").readlines()
    #     if len(self.p_high) == 0:
    #         self.p_high = open("sentences/"+self.select_factor_dic()+"relevance/p_high.txt", "r").readlines()
    #     if len(self.n_low) == 0: 
    #         self.n_low = open("sentences/"+self.select_factor_dic()+"relevance/n_low.txt", "r").readlines()
    #     if len(self.n_mid) == 0:
    #         self.n_mid = open("sentences/"+self.select_factor_dic()+"relevance/n_mid.txt", "r").readlines()
    #     if len(self.n_high) == 0:
    #         self.n_high = open("sentences/"+self.select_factor_dic()+"relevance/n_high.txt", "r").readlines()

    #     if self.relevance < 0.15:
    #         return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")
    #     elif self.relevance < 0.35:
    #         return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
    #     elif self.relevance < 0.5:
    #         return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
    #     elif self.relevance < 0.65:
    #         return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
    #     elif self.relevance < 0.85:
    #         return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
    #     else:
    #         return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
