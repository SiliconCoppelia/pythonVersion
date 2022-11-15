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

    low, mid, high, \
    UI_p_low, UI_p_mid, UI_p_high, UI_n_low, UI_n_mid, UI_n_high,\
    inv_low, inv_mid, inv_high,\
    dis_low, dis_mid, dis_high = ([] for i in range(15))
    
    # def __init__(self, use_intention, input_factor):
    #     self.use_intention = use_intention
    #     self.input_factor=input_factor

    def setSimilarity(self, similarity, UI, inv, dis):
        self.similarity = similarity
        # self.influence = influence
        self.UI = UI
        self.inv = inv
        self.dis = dis


    # def setModerating_factor(self, moderating_factor):
    #     self.moderating_factor = moderating_factor
    


    '''
        This function is used to get the sentence of similarity on UI

        args: 
        - self: the value of similarity
        - influence: influence means the pos/neg influence that similarity makes to UI, 1 menas pos, -1 menas neg
        - UI: the value of UI
        
    '''
    def getSimilarityOnUI(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        

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
        
        
        # # INFLUENCE
        # if(self.influence>0):
        #     if len(self.UI_p_low) == 0: 
        #         self.UI_p_low = open("sentences/similarity/pos/UI_low.txt", "r").readlines()
        #     if len(self.UI_p_mid) == 0:
        #         self.UI_p_mid = open("sentences/similarity/pos/UI_mid.txt", "r").readlines()
        #     if len(self.UI_p_high) == 0:
        #         self.UI_p_high = open("sentences/similarity/pos/UI_high.txt", "r").readlines()

        #     if self.UI < 0.34:
        #         return sentence+self.UI_p_low.pop(randrange(len(self.UI_p_low))).replace("\n", "")
        #     elif self.UI < 0.67:
        #         return sentence+self.UI_p_mid.pop(randrange(len(self.UI_p_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.UI_p_high.pop(randrange(len(self.UI_p_high))).replace("\n", "")
        # else:
        #     if len(self.UI_n_low) == 0: 
        #         self.UI_n_low = open("sentences/similarity/neg/UI_low.txt", "r").readlines()
        #     if len(self.UI_n_mid) == 0:
        #         self.UI_n_mid = open("sentences/similarity/neg/UI_mid.txt", "r").readlines()
        #     if len(self.UI_n_high) == 0:
        #         self.UI_n_high = open("sentences/similarity/neg/UI_high.txt", "r").readlines()

        #     if self.UI < 0.34:
        #         return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_low))).replace("\n", "")
        #     elif self.UI < 0.67:
        #         return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.UI_n_low.pop(randrange(len(self.UI_n_high))).replace("\n", "")
        
    
    
    def getSimilarityOnInv(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.high) == 0:
            self.high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
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

        # # INFLUENCE
        # if(self.influence>0):
        #     if len(self.inv_p_low) == 0: 
        #         self.inv_p_low = open("sentences/similarity/pos/inv_low.txt", "r").readlines()
        #     if len(self.inv_p_mid) == 0:
        #         self.inv_p_mid = open("sentences/similarity/pos/inv_mid.txt", "r").readlines()
        #     if len(self.inv_p_high) == 0:
        #         self.inv_p_high = open("sentences/similarity/pos/inv_high.txt", "r").readlines()

        #     if self.inv < 0.34:
        #         return sentence+self.inv_p_low.pop(randrange(len(self.inv_p_low))).replace("\n", "")
        #     elif self.inv < 0.67:
        #         return sentence+self.inv_p_mid.pop(randrange(len(self.inv_p_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.inv_p_high.pop(randrange(len(self.inv_p_high))).replace("\n", "")
        # else:
        #     if len(self.inv_p_low) == 0: 
        #         self.inv_p_low = open("sentences/similarity/neg/inv_low.txt", "r").readlines()
        #     if len(self.inv_p_mid) == 0:
        #         self.inv_p_mid = open("sentences/similarity/neg/inv_mid.txt", "r").readlines()
        #     if len(self.inv_p_high) == 0:
        #         self.inv_p_high = open("sentences/similarity/neg/inv_high.txt", "r").readlines()

        #     if self.inv < 0.34:
        #         return sentence+self.inv_n_low.pop(randrange(len(self.inv_n_low))).replace("\n", "")
        #     elif self.inv < 0.67:
        #         return sentence+self.inv_n_mid.pop(randrange(len(self.inv_n_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.inv_n_high.pop(randrange(len(self.inv_n_high))).replace("\n", "")

    
    
    def getSimilarityOnDis(self):
        if len(self.low) == 0: 
            self.low = open("sentences/similarity/similarity/low.txt", "r").readlines()
        if len(self.mid) == 0:
            self.mid = open("sentences/similarity/similarity/mid.txt", "r").readlines()
        if len(self.high) == 0:
            self.high = open("sentences/similarity/similarity/high.txt", "r").readlines()

        sentence=""

        if self.similarity < 0.34:
            sentence = self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.similarity < 0.67:
            sentence = self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            sentence = self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")
        
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
        # # INFLUENCE
        # if(self.influence>0):
        #     if len(self.dis_p_low) == 0: 
        #         self.dis_p_low = open("sentences/similarity/pos/dis_low.txt", "r").readlines()
        #     if len(self.dis_p_mid) == 0:
        #         self.dis_p_mid = open("sentences/similarity/pos/dis_mid.txt", "r").readlines()
        #     if len(self.dis_p_high) == 0:
        #         self.dis_p_high = open("sentences/similarity/pos/dis_high.txt", "r").readlines()

        #     if self.dis < 0.34:
        #         return sentence+self.dis_p_low.pop(randrange(len(self.dis_p_low))).replace("\n", "")
        #     elif self.dis < 0.67:
        #         return sentence+self.dis_p_mid.pop(randrange(len(self.dis_p_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.dis_p_high.pop(randrange(len(self.dis_p_high))).replace("\n", "")
        # else:
        #     if len(self.dis_p_low) == 0: 
        #         self.dis_p_low = open("sentences/similarity/neg/dis_low.txt", "r").readlines()
        #     if len(self.dis_p_mid) == 0:
        #         self.dis_p_mid = open("sentences/similarity/neg/dis_mid.txt", "r").readlines()
        #     if len(self.dis_p_high) == 0:
        #         self.dis_p_high = open("sentences/similarity/neg/dis_high.txt", "r").readlines()

        #     if self.dis < 0.34:
        #         return sentence+self.dis_n_low.pop(randrange(len(self.dis_n_low))).replace("\n", "")
        #     elif self.dis < 0.67:
        #         return sentence+self.dis_n_mid.pop(randrange(len(self.dis_n_mid))).replace("\n", "")
        #     else:
        #         return sentence+self.dis_n_high.pop(randrange(len(self.dis_n_high))).replace("\n", "")