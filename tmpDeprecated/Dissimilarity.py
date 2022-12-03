'''
  @Author Yooki ZHANG
  @Date 6/11/2022
  @Description:

'''

from random import random
from random import randrange

class Dissimilarity:

    dissimilarity = 0
    # moderating_factor = ""

    low, mid, high, \
    UI_p_low, UI_p_mid, UI_p_high, UI_n_low, UI_n_mid, UI_n_high,\
    inv_low, inv_mid, inv_high,\
    dis_low, dis_mid, dis_high = ([] for i in range(15))
    
    # def __init__(self, use_intention, input_factor):
    #     self.use_intention = use_intention
    #     self.input_factor=input_factor

    def setDissimilarity(self, dissimilarity, UI, inv, dis):
        self.dissimilarity = dissimilarity
        # self.influence = influence
        self.UI = UI
        self.inv = inv
        self.dis = dis


    '''
        This function is used to get the sentence of dissimilarity on UI

        args: 
        - self: the value of dissimilarity
        - influence: influence means the pos/neg influence that dissimilarity makes to UI, 1 menas pos, -1 menas neg
        - UI: the value of UI
        
    '''
    def getDissimilarityOnUI(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/dissimilarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/dissimilarity/mid.txt", "r").readlines()
        if len(self.high) == 0:
            self.high = open("sentences/similarity/dissimilarity/high.txt", "r").readlines()

        sentence=""

        if self.dissimilarity < 0.34:
            sentence = self.low.pop(randrange(len(self.low))).replace("\n", "")
        elif self.dissimilarity < 0.67:
            sentence = self.mid.pop(randrange(len(self.mid))).replace("\n", "")
        else:
            sentence = self.high.pop(randrange(len(self.high))).replace("\n", "")
        

        if len(self.UI_p_low) == 0: 
            self.UI_p_low = open("sentences/similarity/UI_p_low.txt", "r").readlines()
        if len(self.UI_p_mid) == 0:
            self.UI_p_mid = open("sentences/similarity/UI_p_mid.txt", "r").readlines()
        if len(self.UI_p_high) == 0:
            self.UI_p_high = open("sentences/similarity/UI_p_high.txt", "r").readlines()
        if len(self.UI_n_low) == 0: 
            self.UI_n_low = open("sentences/similarity/UI_n_low.txt", "r").readlines()
        if len(self.UI_n_mid) == 0:
            self.UI_n_mid = open("sentences/similarity/UI_n_mid.txt", "r").readlines()
        if len(self.UI_n_high) == 0:
            self.UI_n_high = open("sentences/similarity/UI_n_high.txt", "r").readlines()

        if self.UI > 0 :
            if self.UI < 0.34:
                return sentence+self.UI_p_low.pop(randrange(len(self.UI_p_low))).replace("\n", "")
            elif self.UI < 0.67:
                return sentence+self.UI_p_mid.pop(randrange(len(self.UI_p_mid))).replace("\n", "")
            else:
                return sentence+self.UI_p_high.pop(randrange(len(self.UI_p_high))).replace("\n", "")
        else:        
            if self.UI > -0.34:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_low))).replace("\n", "")
            elif self.UI > -0.67:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_mid))).replace("\n", "")
            else:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_high))).replace("\n", "")

    
    def getDissimilarityOnInv(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/dissimilarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/dissimilarity/mid.txt", "r").readlines()
        if len(self.high) == 0:
            self.high = open("sentences/similarity/dissimilarity/high.txt", "r").readlines()

        sentence=""

        if self.dissimilarity < 0.34:
            sentence = self.low.pop(randrange(len(self.low))).replace("\n", "")
        elif self.dissimilarity < 0.67:
            sentence = self.mid.pop(randrange(len(self.mid))).replace("\n", "")
        else:
            sentence = self.high.pop(randrange(len(self.high))).replace("\n", "")
        
        if len(self.inv_low) == 0: 
            self.inv_low = open("sentences/similarity/inv_low.txt", "r").readlines()
        if len(self.inv_mid) == 0:
            self.inv_mid = open("sentences/similarity/inv_mid.txt", "r").readlines()
        if len(self.inv_high) == 0:
            self.inv_high = open("sentences/similarity/inv_high.txt", "r").readlines()
        if self.inv < 0.34:
            return sentence+self.inv_low.pop(randrange(len(self.inv_low))).replace("\n", "")
        elif self.inv < 0.67:
            return sentence+self.inv_mid.pop(randrange(len(self.inv_mid))).replace("\n", "")
        else:
            return sentence+self.inv_high.pop(randrange(len(self.inv_high))).replace("\n", "")
    
    
    def getDissimilarityOnDis(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/dissimilarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/dissimilarity/mid.txt", "r").readlines()
        if len(self.high) == 0:
            self.high = open("sentences/similarity/dissimilarity/high.txt", "r").readlines()

        sentence=""

        if self.dissimilarity < 0.34:
            sentence = self.low.pop(randrange(len(self.low))).replace("\n", "")
        elif self.dissimilarity < 0.67:
            sentence = self.mid.pop(randrange(len(self.mid))).replace("\n", "")
        else:
            sentence = self.high.pop(randrange(len(self.high))).replace("\n", "")
        
        if len(self.dis_low) == 0: 
            self.dis_low = open("sentences/similarity/dis_low.txt", "r").readlines()
        if len(self.dis_mid) == 0:
            self.dis_mid = open("sentences/similarity/dis_mid.txt", "r").readlines()
        if len(self.dis_high) == 0:
            self.dis_high = open("sentences/similarity/dis_high.txt", "r").readlines()
        if self.dis < 0.34:
            return sentence+self.dis_low.pop(randrange(len(self.dis_low))).replace("\n", "")
        elif self.dis < 0.67:
            return sentence+self.dis_mid.pop(randrange(len(self.dis_mid))).replace("\n", "")
        else:
            return sentence+self.dis_high.pop(randrange(len(self.dis_high))).replace("\n", "")
