from validator import Validator

class XORCipher:
    def __init__(self, cipher):
        super().__init__()
        self.cipher = cipher
        self.validator = Validator()
        
    
    def find_xor_bit(self):
        temp_cipher = self.cipher[:30]
        result = []
        for i in range(256):
            temp_value = self.check(temp_cipher,chr(i))
            if temp_value:
                result.append(i)
        return result
    
    
    def decode(self, cipher, xor_string):
        if(len(cipher) != len(xor_string)):
            raise ValueError("String length mismatch")
        result = []
        c1 = cipher
        c2 = xor_string.encode()
        for i in range(len(cipher)):
            result.append(chr(c1[i] ^ c2[i]))
        return "".join(result)
    
    
    def check(self, cipher, character):
        temp_val = self.decode(cipher,character*len(cipher))
        if self.validator.check(temp_val):
            return temp_val
    
    
    def crack_cipher(self):
        result = []
        for i in self.find_xor_bit():
            decoded_string = self.decode(self.cipher,chr(i)*len(self.cipher))
            result.append(XOROutput(i,decoded_string))
        return result
    
        
class XOROutput:
    def __init__(self, xor_bit_value, decoded_string):
        super().__init__()
        self.xor_bit_value = xor_bit_value
        self.decoded_string = decoded_string
        
    def print(self):
        print("XOR Bit Value:", self.xor_bit_value, chr(self.xor_bit_value))
        print("Decoded String:", self.decoded_string)