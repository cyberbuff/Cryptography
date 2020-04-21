from abc import ABC,abstractmethod

class Cipher(ABC):
    def __init__(self,cipher):
        super().__init__()
        self.cipher = cipher


    @abstractmethod
    def bruteforce(self):
        pass
    
    
    @staticmethod
    def encode(text,key):
        pass
    
    
    @staticmethod
    def decode(cipher, key):
        pass
    
    # TODO: Enable Validate Methods after fixing validator.py
    # @abstractmethod
    # def validate(self,decoded_string):
    #     pass
    
    
class CipherOutput(ABC):
    def __init__(self, key, output):
        self.key = key
        self.output = output
    
    @abstractmethod
    def print(self):
        pass