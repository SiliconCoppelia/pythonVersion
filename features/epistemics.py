from keytotext import pipeline
from random import randrange

class epistemics():
    def __init__(self, epistemics_value):
        self.epistemics=epistemics_value
        self.indi_epis_low, self.indi_epis_mid, self.indi_epis_high, self.contra_epis_low, self.contra_epis_mid, self.contra_epis_high = ([] for i in range(6))
    
    def generation():
        print()
        
        nlp = pipeline("k2t-base")  #loading the pre-trained model
        params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":3, "early_stopping":True}    #decoding params
        print (nlp(['You', 'look', 'like', 'human'], **params))  #keywords

    #-----------------------------INDICATIVE-----------------------------#

    def get_indicative_epis_encoding(self):
		# Load corpus if all variants in one dimension are used up
        if len(self.indi_epis_low) == 0: 
            self.indi_epis_low = open("./sentences/epistemics/epi_ind_low.txt", "r").readlines()
        if len(self.indi_epis_mid) == 0:
            self.indi_epis_mid = open("./sentences/epistemics/epi_ind_mid.txt", "r").readlines()
        if len(self.indi_epis_high) == 0:
            self.indi_epis_high = open("./sentences/epistemics/epi_ind_high.txt", "r").readlines()      
        # Get Encding
        if self.epistemics < 0.34:
            return self.indi_epis_low.pop(randrange(len(self.indi_epis_low))).replace("\n", "")
        elif self.epistemics >= 0.34 and self.epistemics < 0.67:
            return self.indi_epis_mid.pop(randrange(len(self.indi_epis_mid))).replace("\n", "")
        else:
            return self.indi_epis_high.pop(randrange(len(self.indi_epis_high))).replace("\n", "")

    #-----------------------------INDICATIVE-----------------------------#
    
    def get_contra_epis_encoding(self):
	# Load corpus if all variants in one dimension are used up
        if len(self.contra_epis_low) == 0: 
            self.contra_epis_low = open("./sentences/epistemics/epi_con_low.txt", "r").readlines()
        if len(self.contra_epis_mid) == 0:
            self.contra_epis_mid = open("./sentences/epistemics/epi_con_mid.txt", "r").readlines()
        if len(self.contra_epis_high) == 0:
            self.contra_epis_high = open("./sentences/epistemics/epi_con_high.txt", "r").readlines()      
        # Get Encding
        if self.epistemics < 0.34:
            return self.contra_epis_low.pop(randrange(len(self.contra_epis_low))).replace("\n", "")
        elif self.epistemics >= 0.34 and self.epistemics < 0.67:
            return self.contra_epis_mid.pop(randrange(len(self.contra_epis_mid))).replace("\n", "")
        else:
            return self.contra_epis_high.pop(randrange(len(self.contra_epis_high))).replace("\n", "")

    # def get_epistemics_encoding():
    # self.generation()
# epi= epistemics(0.1)
# print(epi.get_indicative_epis_encoding())
# print(epi.get_contra_epis_encoding())
