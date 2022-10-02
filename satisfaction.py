'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:

'''
from readFromTxt import get_line_context;
from readFromTxt import get_line_num;
from readFromTxt import get_random_line;

class Satisfaction:

    def __init__(self, satisfaction, input_factor):
        self.satisfaction = satisfaction
        self.input_factor=input_factor
    
    def select_factor_dic(self):
        if(self.input_factor=="ethics"): return "ethics/"
        elif(self.input_factor=="affordance"): return "affordance/"
        elif(self.input_factor=="aesthetics"): return "aesthetics/"
        else: return "epistemics/"
    
    def select_sentence_file(self):
        if(self.satisfaction<=0.15): return "n_high"
        elif(self.satisfaction<0.35): return "n_mid"
        elif(self.satisfaction<0.5): return "n_low"
        elif(self.satisfaction<0.65): return "p_low"
        elif(self.satisfaction<0.85): return "p_mid"
        else: return "p_high"
    
    def get_sentences_from_file(self):
        file_path="sentences/"+self.select_factor_dic()+"satisfaction/"+self.select_sentence_file()+".txt"
        line_num = get_line_num(file_path)
        selected_line = get_random_line(line_num)
        sentence = get_line_context(file_path, selected_line)
        return sentence