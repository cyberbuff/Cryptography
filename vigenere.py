from caesar import Caesar
from freqanalyzer import FrequencyAnalyzer
from utils import sort_dict_by_values

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


# def encode_dictionary():
#   d = {}
#   str = string.ascii_lowercase
#   for i in range(26):
#     for j in range(26):
#       d[str[i]+str[j]] = str[(i+j)%26]
#   return d

# def decode_dictionary():
#   d = {}
#   str = string.ascii_lowercase
#   for i in range(26):
#     for j in range(26):
#       d[str[i]+str[j]] = str[i-j]
#   return d

# d2 = decode_dictionary()
# str = "a'z uxyyi qmict fxk".lower()
# print(d2['ia'],d2['mz'])

# import string
# from statistics import mean
# from validator import FrequencyAnalyzer 
# from vigenere import Vigenere
# from utils import *


# def get_top_IC(text, top_number=3):
#     d2 = {}
#     for i in range(2,15):
#         arr = splitstrings(text,i)
#         sum_array = mean([findIC(i) for i in arr])
#         d2[i] = sum_array
#     print(d2)
#     return sort_dict_by_values(d2,reverse=True)[:3]

# # text = "vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"
# # for i in [7]:
# #     a = splitstrings(text,i)
# #     for j in a:
# #         # print(a)
# #         x = Vigenere.decode_chi(j)
# #         for j,k in x:
# #             print(string.ascii_lowercase[j], end= " ")
# #         print()
        
# with open("part5.txt","r") as f:
#     file = f.readlines()
#     max = 0
#     txt = ""
#     for i in file:
#         if len(i) > max:
#             max = len(i)
#             txt = i
#     # txt = (process_text(txt))
#     print(txt)
#     z = get_top_IC(txt)
#     print(z)
#     for i,_ in z:
#         print(i)
#         a = splitstrings(txt,i)
#         for j in a:
#             x = Vigenere.decode_chi(j)
#             for k,l in x:
#                 print(string.ascii_lowercase[k], end= " ")
#             print()

