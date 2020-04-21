import string
from utils import sort_dict_by_values
from freqanalyzer import FrequencyAnalyzer
from cipher import *
import sys

class CaesarOutput(CipherOutput):
    def print(self):
        print("ROT Value: {}".format(self.key))
        print("Decoded String: {}".format(self.output))


class Caesar(Cipher):
    def bruteforce(self):
        shift_value = self.__find_shift_value(self.cipher)
        decoded_string = self.decode(self.cipher,shift_value)
        return CaesarOutput(shift_value,decoded_string)


    @staticmethod
    def decode(cipher, shift):
        def create_dictionary(shift):
            caesar_dict = (lambda x: {x[i]:x[(i+shift)%len(x)] for i in range(len(x))})
            # {**x,**y} merges dictionary x and y.
            return {**caesar_dict(string.ascii_lowercase),**caesar_dict(string.ascii_uppercase)}
        cipher_dict = create_dictionary(shift)
        return "".join([cipher_dict[i] if i in string.ascii_letters else i for i in cipher])    


    def __calculate_frequency(self, cipher, key):
        decoded_string = self.decode(cipher,key)
        return FrequencyAnalyzer.chisquaredstatistic(decoded_string)


    def __find_shift_value(self, cipher):
        temp_cipher = " ".join(cipher.split()[:20])
        scores_list = [self.__calculate_frequency(temp_cipher,i) for i in range(26)]
        scores_dict = dict(zip(range(26),scores_list))
        return sort_dict_by_values(scores_dict)[0][0]
    
    
    # TODO: Fix validator.py 
    # def validate(self,decoded_string):
    #     return Validator.is_sentence_valid(decoded_string)
