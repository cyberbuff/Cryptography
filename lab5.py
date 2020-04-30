from caesar import Caesar
from freqanalyzer import FrequencyAnalyzer
from utils import *
from statistics import mean
from validator import Validator


class Vigenere:
    def __init__(self, cipher):
        super().__init__()
        self.cipher = cipher
        
    
    @staticmethod 
    def decode_chi(cipher):
        d2 = {}
        arr = []
        for j in range(26): 
            k = (26-j)%26
            temp = Caesar.decode(cipher,j)
            sum = FrequencyAnalyzer.chisquaredstatistic(temp)
            d2[k] = sum
        return sort_dict_by_values(d2)[:3]


def get_top_IC(text, top_number=3):
    text = text.lower()
    d2 = {}
    for i in range(2,15):
        arr = split_strings(text,i)
        arr = [i for i in arr if len(i) != 0]
        if len(arr) != 0:
            sum_array = mean([FrequencyAnalyzer.findIC(i) for i in arr])
            d2[i] = sum_array
    return sort_dict_by_values(d2,reverse=True)[:5]
        
def process_text(text):
    return "".join([i for i in text if i in string.ascii_letters]).lower()    

with open("part5.txt","r") as f:
    file = f.read()
    d2 = {}
    for i in range(2,15):
        d2[i] = []
    text = process_text(file)
    temp_dict = get_top_IC(text)
    
    possible_keys = {}
    for i,_ in temp_dict:
        a = split_strings(file,i)
        result = []
        for j in a:
            x = Vigenere.decode_chi(j)
            result.append(string.ascii_letters[x[0][0]])
        result = "".join(result)
        if Validator.is_valid_word(result):
            possible_keys[i] = result
    
    print("Possible Keys")
    for i,j in possible_keys.items():
        print("Key:",j)