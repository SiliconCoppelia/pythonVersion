'''
  @Author Yooki ZHANG
  @Date 6/11/2022
  @Description:

'''

from random import random
from random import randrange

class Similarity:

    similarity = 0
    # moderating_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high, UI_low, UI_mid, UI_high, inv_low, inv_mid, inv_high, dis_low, dis_mid, dis_high = ([] for i in range(15))
    
    # def __init__(self, use_intention, input_factor):
    #     self.use_intention = use_intention
    #     self.input_factor=input_factor

    def setSimilarity(self, similarity):
        self.similarity = similarity

    # def setModerating_factor(self, moderating_factor):
    #     self.moderating_factor = moderating_factor
    


    '''
        This function is used to get the sentence of similarity on UI

        args: 
        - self: the value of similarity
        - influence: influence means the pos/neg influence that similarity makes to UI, 1 menas pos, -1 menas neg
        - UI: the value of UI
        
    '''
    def getSimilarityOnUI(self, influence, UI):
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/similarity/low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/similarity/mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/similarity/high.txt", "r").readlines()
        
        # INFLUENCE
        if(influence>0):
            if len(self.UI_low) == 0: 
                self.UI_low = open("sentences/similarity/pos/UI_low.txt", "r").readlines()
            if len(self.UI_mid) == 0:
                self.UI_mid = open("sentences/similarity/pos/UI_mid.txt", "r").readlines()
            if len(self.UI_high) == 0:
                self.UI_high = open("sentences/similarity/pos/UI_high.txt", "r").readlines()
        else:
            if len(self.UI_low) == 0: 
                self.UI_low = open("sentences/similarity/neg/UI_low.txt", "r").readlines()
            if len(self.UI_mid) == 0:
                self.UI_mid = open("sentences/similarity/neg/UI_mid.txt", "r").readlines()
            if len(self.UI_high) == 0:
                self.UI_high = open("sentences/similarity/neg/UI_high.txt", "r").readlines()
        
        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")

        if UI < 0.34:
            return sentence+self.UI_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif UI < 0.67:
            return sentence+self.UI_low.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return sentence+self.UI_low.pop(randrange(len(self.p_high))).replace("\n", "")
    
    
    def getSimilarityOnInv(self):
        

    
    def getSimilarityOnDis(self):