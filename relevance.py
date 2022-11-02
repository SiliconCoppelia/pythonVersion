'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:

'''
from random import random
from random import randrange

class Relevance:

    relevance = 0
    input_factor = ""
    
    # def __init__(self, relevance, input_factor):
    #     self.relevance = relevance
    #     self.input_factor=input_factor

    def setRelevance(self, relevance):
        self.relevance = relevance

    def setInputFactor(self, input_factor):
        self.input_factor = input_factor
    
    def select_factor_dic(self):
        if(self.input_factor=="ethics"): return "ethics/"
        elif(self.input_factor=="affordance"): return "affordance/"
        elif(self.input_factor=="aesthetics"): return "aesthetics/"
        else: return "epistemics/"

    def select_sentence_file(self):
        if(self.relevance<=0.15): return "n_high"
        elif(self.relevance<0.35): return "n_mid"
        elif(self.relevance<0.5): return "n_low"
        elif(self.relevance<0.65): return "p_low"
        elif(self.relevance<0.85): return "p_mid"
        else: return "p_high"

    def loadCorpus(self):
        corpus_p_low="sentences/"+self.select_factor_dic()+"relevance/p_low.txt"
        corpus_n_low="sentences/"+self.select_factor_dic()+"relevance/n_low.txt"
        corpus_p_mid="sentences/"+self.select_factor_dic()+"relevance/p_mid.txt"
        corpus_n_mid="sentences/"+self.select_factor_dic()+"relevance/n_mid.txt"
        corpus_p_high="sentences/"+self.select_factor_dic()+"relevance/p_high.txt"
        corpus_n_high="sentences/"+self.select_factor_dic()+"relevance/n_high.txt"
        self.p_low = open(corpus_p_low, "r").readlines()
        self.p_mid = open(corpus_p_mid, "r").readlines()
        self.p_high = open(corpus_p_high, "r").readlines()
        self.n_low = open(corpus_n_low, "r").readlines()
        self.n_mid = open(corpus_n_mid, "r").readlines()
        self.n_high = open(corpus_n_high, "r").readlines()

    def getrelevance(self):
        if len(self.p_low) == 0 or len(self.p_mid) == 0 or len(self.p_high) == 0 or len(self.n_low) == 0 or len(self.n_mid) == 0 or len(self.n_high) == 0:
            self.loadCorpus()
        if self.relevance < 0.15:
            return self.n_high.pop(randrange(len(self.n_high))).replace("\n", "")
        elif self.relevance < 0.35:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        elif self.relevance < 0.5:
            return self.n_low.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.relevance < 0.65:
            return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.relevance < 0.85:
            return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")


# from readFromTxt import get_line_context;
# from readFromTxt import get_line_num;
# from readFromTxt import get_random_line;

# class Relevance:

#     def __init__(self, rel, input_factor):
#         self.rel = rel
#         self.input_factor=input_factor
    
#     def select_factor_dic(self):
#         if(self.input_factor=="ethics"): return "ethics/"
#         elif(self.input_factor=="affordance"): return "affordance/"
#         elif(self.input_factor=="aesthetics"): return "aesthetics/"
#         else: return "epistemics/"
    
#     def select_sentence_file(self):
#         if(self.rel<=0.15): return "n_high"
#         elif(self.rel<0.35): return "n_mid"
#         elif(self.rel<0.5): return "n_low"
#         elif(self.rel<0.65): return "p_low"
#         elif(self.rel<0.85): return "p_mid"
#         else: return "p_high"
    
#     def get_sentences_from_file(self):
#         file_path="sentences/"+self.select_factor_dic()+"relevance/"+self.select_sentence_file()+".txt"
#         line_num = get_line_num(file_path)
#         selected_line = get_random_line(line_num)
#         sentence = get_line_context(file_path, selected_line)
#         return sentence