import string
from validator import Validator

class CaesarOutput:
    def __init__(self, rot_value, output):
        super().__init__()
        self.rot_value = rot_value
        self.output = output
    
    def print(self):
        print("ROT Value: {}".format(self.rot_value))
        print("Decoded String: {}".format(self.output))
    
    
class Caesar:
    def __init__(self,cipher):
        super().__init__()
        self.cipher = cipher
        self.validator = Validator()
        
    
    def crack(self):
        possible_shifts = self.find_shift_value(self.cipher)
        possible_outputs = []
        for i in possible_shifts:
            possible_outputs.append(CaesarOutput(i, self.decode(self.cipher,i)))
        return possible_outputs

    
    def find_shift_value(self, cipher):
        temp_cipher = " ".join(cipher.split()[:10])
        possible_shifts = []
        for i in range(26):
            if self.check(temp_cipher,i):
                possible_shifts.append(i)
        return possible_shifts


    def create_dictionary(self,shift):
        dict = {}
        characters = string.ascii_lowercase
        characters2 = string.ascii_uppercase
        for i in range(len(characters)):
            dict[characters[i]] = characters[(i+shift)%len(characters)]
            dict[characters2[i]] = characters2[(i+shift)%len(characters)]
        return dict


    def decode(self, cipher, shift):
        cipher_dict = self.create_dictionary(shift)
        b = ""
        for i in cipher:
            if i in string.ascii_letters:
                b += (cipher_dict[i])
            else:
                b += i
        return b


    def is_valid(self, decoded_string):
        return self.validator.is_sentence_valid(decoded_string)


    def check(self, cipher, shift):
        decoded_string = self.decode(cipher,shift)
        if self.is_valid(decoded_string):
            return decoded_string