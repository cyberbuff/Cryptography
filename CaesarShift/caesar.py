import enchant
import string
import sys

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
        
    
    def crack(self):
        possible_shifts = self.find_shift_value(self.cipher)
        possible_outputs = []
        for i in possible_shifts:
            possible_outputs.append(CaesarOutput(i, self.check("".join(cipher),i)))
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


    def check(self, cipher, shift):
        decoded_string = self.decode(cipher,shift)
        b = []
        dictionary = enchant.Dict("en_US")
        tempArray = decoded_string.split()
        for i in tempArray:
            b.append(dictionary.check(i))
        if (sum(b) > len(tempArray)/2):
            return decoded_string


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1],"r") as f:
                cipher = "".join(f.readlines())
                caesar_objects = Caesar(cipher).crack()
                for i in caesar_objects:
                    i.print()
        except FileNotFoundError:
            print("File Not Found.")
    else:
        print("Usage: python3 {} <cipher-file>".format(sys.argv[0]))
