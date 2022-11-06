'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:

'''
from random import random
from random import randrange

class Valence:

    valence = 0
    input_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high = ([] for i in range(6))
    
    # def __init__(self, valence, input_factor):
    #     self.valence = valence
    #     self.input_factor=input_factor

    def setValence(self, valence):
        self.valence = valence

    def setInputFactor(self, input_factor):
        self.input_factor = input_factor
    
    def select_factor_dic(self):
        if(self.input_factor=="ethics"): return "ethics/"
        elif(self.input_factor=="affordance"): return "affordance/"
        elif(self.input_factor=="aesthetics"): return "aesthetics/"
        else: return "epistemics/"
    
    def getPosValence(self):
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/"+self.select_factor_dic()+"valence/p_low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/"+self.select_factor_dic()+"valence/p_mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/"+self.select_factor_dic()+"valence/p_high.txt", "r").readlines()

        if self.valence < 0.34:
            return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.valence < 0.67:
            return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
    def getNegValence(self):
        if len(self.n_low) == 0: 
            self.n_low = open("sentences/"+self.select_factor_dic()+"valence/n_low.txt", "r").readlines()
        if len(self.n_mid) == 0:
            self.n_mid = open("sentences/"+self.select_factor_dic()+"valence/n_mid.txt", "r").readlines()
        if len(self.n_high) == 0:
            self.n_high = open("sentences/"+self.select_factor_dic()+"valence/n_high.txt", "r").readlines()

        if self.valence < 0.34:
            return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.valence < 0.67:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        else:
            return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")

    # def getValence(self):
    #     if len(self.p_low) == 0: 
    #         self.p_low = open("sentences/"+self.select_factor_dic()+"valence/p_low.txt", "r").readlines()
    #     if len(self.p_mid) == 0:
    #         self.p_mid = open("sentences/"+self.select_factor_dic()+"valence/p_mid.txt", "r").readlines()
    #     if len(self.p_high) == 0:
    #         self.p_high = open("sentences/"+self.select_factor_dic()+"valence/p_high.txt", "r").readlines()
    #     if len(self.n_low) == 0: 
    #         self.n_low = open("sentences/"+self.select_factor_dic()+"valence/n_low.txt", "r").readlines()
    #     if len(self.n_mid) == 0:
    #         self.n_mid = open("sentences/"+self.select_factor_dic()+"valence/n_mid.txt", "r").readlines()
    #     if len(self.n_high) == 0:
    #         self.n_high = open("sentences/"+self.select_factor_dic()+"valence/n_high.txt", "r").readlines()


    #     if self.valence < 0.15:
    #         return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")
    #     elif self.valence < 0.35:
    #         return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
    #     elif self.valence < 0.5:
    #         return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
    #     elif self.valence < 0.65:
    #         return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
    #     elif self.valence < 0.85:
    #         return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
    #     else:
    #         return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")