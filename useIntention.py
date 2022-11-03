'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:

'''

from random import random
from random import randrange

class UseIntention:

    use_intention = 0
    input_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high = ([] for i in range(6))
    
    # def __init__(self, use_intention, input_factor):
    #     self.use_intention = use_intention
    #     self.input_factor=input_factor

    def setUseIntention(self, use_intention):
        self.use_intention = use_intention

    def setInputFactor(self, input_factor):
        self.input_factor = input_factor
    
    def select_factor_dic(self):
        if(self.input_factor=="ethics"): return "ethics/"
        elif(self.input_factor=="affordance"): return "affordance/"
        elif(self.input_factor=="aesthetics"): return "aesthetics/"
        else: return "epistemics/"
    
    def getUseIntention(self):
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/use_intention/p_low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/use_intention/p_mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/use_intention/p_high.txt", "r").readlines()
        if len(self.n_low) == 0: 
            self.n_low = open("sentences/use_intention/n_low.txt", "r").readlines()
        if len(self.n_mid) == 0:
            self.n_mid = open("sentences/use_intention/n_mid.txt", "r").readlines()
        if len(self.n_high) == 0:
            self.n_high = open("sentences/use_intention/n_high.txt", "r").readlines()

    # def getUseIntention(self):
    #     if len(self.p_low) == 0: 
    #         self.p_low = open("sentences/"+self.select_factor_dic()+"use_intention/p_low.txt", "r").readlines()
    #     if len(self.p_mid) == 0:
    #         self.p_mid = open("sentences/"+self.select_factor_dic()+"use_intention/p_mid.txt", "r").readlines()
    #     if len(self.p_high) == 0:
    #         self.p_high = open("sentences/"+self.select_factor_dic()+"use_intention/p_high.txt", "r").readlines()
    #     if len(self.n_low) == 0: 
    #         self.n_low = open("sentences/"+self.select_factor_dic()+"use_intention/n_low.txt", "r").readlines()
    #     if len(self.n_mid) == 0:
    #         self.n_mid = open("sentences/"+self.select_factor_dic()+"use_intention/n_mid.txt", "r").readlines()
    #     if len(self.n_high) == 0:
    #         self.n_high = open("sentences/"+self.select_factor_dic()+"use_intention/n_high.txt", "r").readlines()

        
        if self.use_intention < 0.15:
            return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")
        elif self.use_intention < 0.35:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        elif self.use_intention < 0.5:
            return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.use_intention < 0.65:
            return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.use_intention < 0.85:
            return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")

