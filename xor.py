# from validator import Validator
from cipher import *
from freqanalyzer import FrequencyAnalyzer
from utils import sort_dict_by_values
from itertools import cycle

class XORCipher(Cipher):
    def find_xor_bit(self):
        temp_cipher = self.cipher[:30]
        scores_dict = {}
        for i in range(256):
            scores_dict[i] = FrequencyAnalyzer.calculate_frequency(self.decode(temp_cipher,i))
        return sort_dict_by_values(scores_dict,reverse=True)[0][0]
    
    
    @staticmethod
    def xor(cipher,key):
        if isinstance(key,int):
            key = bytes([key])
        if isinstance(cipher,str):
            cipher = cipher.encode()
        if isinstance(key,str):
            key = key.encode()
        return "".join([chr(x^y) for x,y in zip(cipher,cycle(key))])


    @staticmethod
    def decode(cipher, key):
        return XORCipher.xor(cipher,key)

    
    @staticmethod
    def encode(cipher,key):
        return XORCipher.xor(cipher,key)
    
    
    def bruteforce(self):
        xor_bit = self.find_xor_bit()
        decoded_string = self.decode(self.cipher,xor_bit)
        return XOROutput(xor_bit,decoded_string)
    
        
class XOROutput(CipherOutput):
    def print(self):
        print("XOR Bit Value:", self.key, chr(self.key))
        print("Decoded String:", self.output)