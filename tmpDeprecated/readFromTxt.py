'''
  @Author Yooki ZHANG
  @Date 31/9/2022
  @Description:
  
'''

import linecache
import random

# get content from a specific line
def get_line_context(file_path, line_number):
    return linecache.getline(file_path, line_number).strip()

# get the number of lines contained in txt
def get_line_num(file_path):
    return len(open(file_path,'rU').readlines())

def get_random_line(max_num):
    return random.randint(1,max_num)