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

    p_low, p_mid, p_high, n_low, n_mid, n_high, \
    UI_p_low, UI_p_mid, UI_p_high, UI_n_low, UI_n_mid, UI_n_high,\
    inv_p_low, inv_p_mid, inv_p_high, inv_n_low, inv_n_mid, inv_n_high,\
    dis_p_low, dis_p_mid, dis_p_high, dis_n_low, dis_n_mid, dis_n_high = ([] for i in range(24))
    
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
            self.p_low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
        # INFLUENCE
        if(influence>0):
            if len(self.UI_p_low) == 0: 
                self.UI_p_low = open("sentences/similarity/pos/UI_low.txt", "r").readlines()
            if len(self.UI_p_mid) == 0:
                self.UI_p_mid = open("sentences/similarity/pos/UI_mid.txt", "r").readlines()
            if len(self.UI_p_high) == 0:
                self.UI_p_high = open("sentences/similarity/pos/UI_high.txt", "r").readlines()

            if UI < 0.34:
                return sentence+self.UI_p_low.pop(randrange(len(self.UI_p_low))).replace("\n", "")
            elif UI < 0.67:
                return sentence+self.UI_p_low.pop(randrange(len(self.UI_p_mid))).replace("\n", "")
            else:
                return sentence+self.UI_p_low.pop(randrange(len(self.UI_p_high))).replace("\n", "")
        else:
            if len(self.UI_p_low) == 0: 
                self.UI_p_low = open("sentences/similarity/neg/UI_low.txt", "r").readlines()
            if len(self.UI_p_mid) == 0:
                self.UI_p_mid = open("sentences/similarity/neg/UI_mid.txt", "r").readlines()
            if len(self.UI_p_high) == 0:
                self.UI_p_high = open("sentences/similarity/neg/UI_high.txt", "r").readlines()

            if UI < 0.34:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_low))).replace("\n", "")
            elif UI < 0.67:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_mid))).replace("\n", "")
            else:
                return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_high))).replace("\n", "")
        
    
    
    def getSimilarityOnInv(self, influence, inv):
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
        # INFLUENCE
        if(influence>0):
            if len(self.inv_p_low) == 0: 
                self.inv_p_low = open("sentences/similarity/pos/inv_low.txt", "r").readlines()
            if len(self.inv_p_mid) == 0:
                self.inv_p_mid = open("sentences/similarity/pos/inv_mid.txt", "r").readlines()
            if len(self.inv_p_high) == 0:
                self.inv_p_high = open("sentences/similarity/pos/inv_high.txt", "r").readlines()

            if inv < 0.34:
                return sentence+self.inv_p_low.pop(randrange(len(self.inv_p_low))).replace("\n", "")
            elif inv < 0.67:
                return sentence+self.inv_p_low.pop(randrange(len(self.inv_p_mid))).replace("\n", "")
            else:
                return sentence+self.inv_p_low.pop(randrange(len(self.inv_p_high))).replace("\n", "")
        else:
            if len(self.inv_p_low) == 0: 
                self.inv_p_low = open("sentences/similarity/neg/inv_low.txt", "r").readlines()
            if len(self.inv_p_mid) == 0:
                self.inv_p_mid = open("sentences/similarity/neg/inv_mid.txt", "r").readlines()
            if len(self.inv_p_high) == 0:
                self.inv_p_high = open("sentences/similarity/neg/inv_high.txt", "r").readlines()

            if inv < 0.34:
                return sentence+self.inv_n_low.pop(randrange(len(self.inv_n_low))).replace("\n", "")
            elif inv < 0.67:
                return sentence+self.inv_n_low.pop(randrange(len(self.inv_n_mid))).replace("\n", "")
            else:
                return sentence+self.inv_n_low.pop(randrange(len(self.inv_n_high))).replace("\n", "")

    
    
    def getSimilarityOnDis(self, influence, dis):
        if len(self.p_low) == 0: 
            self.p_low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
        # INFLUENCE
        if(influence>0):
            if len(self.dis_p_low) == 0: 
                self.dis_p_low = open("sentences/similarity/pos/dis_low.txt", "r").readlines()
            if len(self.dis_p_mid) == 0:
                self.dis_p_mid = open("sentences/similarity/pos/dis_mid.txt", "r").readlines()
            if len(self.dis_p_high) == 0:
                self.dis_p_high = open("sentences/similarity/pos/dis_high.txt", "r").readlines()

            if dis < 0.34:
                return sentence+self.dis_p_low.pop(randrange(len(self.dis_p_low))).replace("\n", "")
            elif dis < 0.67:
                return sentence+self.dis_p_low.pop(randrange(len(self.dis_p_mid))).replace("\n", "")
            else:
                return sentence+self.dis_p_low.pop(randrange(len(self.dis_p_high))).replace("\n", "")
        else:
            if len(self.dis_p_low) == 0: 
                self.dis_p_low = open("sentences/similarity/neg/dis_low.txt", "r").readlines()
            if len(self.dis_p_mid) == 0:
                self.dis_p_mid = open("sentences/similarity/neg/dis_mid.txt", "r").readlines()
            if len(self.dis_p_high) == 0:
                self.dis_p_high = open("sentences/similarity/neg/dis_high.txt", "r").readlines()

            if dis < 0.34:
                return sentence+self.dis_n_low.pop(randrange(len(self.dis_n_low))).replace("\n", "")
            elif dis < 0.67:
                return sentence+self.dis_n_low.pop(randrange(len(self.dis_n_mid))).replace("\n", "")
            else:
                return sentence+self.dis_n_low.pop(randrange(len(self.dis_n_high))).replace("\n", "")