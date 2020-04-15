import enchant
import string
import sys

def find_shift_value(cipher):
    temp_cipher = " ".join(cipher.split()[:10])
    possible_shifts = []
    for i in range(26):
        if check(temp_cipher,i):
            possible_shifts.append(i)
    return possible_shifts  
    
    
def create_dictionary(shift):
    dict = {}
    characters = string.ascii_lowercase
    characters2 = string.ascii_uppercase
    for i in range(len(characters)):
        dict[characters[i]] = characters[(i+shift)%len(characters)]
        dict[characters2[i]] = characters2[(i+shift)%len(characters)]
    return dict


def decode(cipher, shift):
    cipher_dict = create_dictionary(shift)
    b = ""
    for i in cipher:
        if i in string.ascii_letters:
            b += (cipher_dict[i])
        else:
            b += i
    return b


def check(cipher,shift):
    decoded_string = decode(cipher,shift)
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
                cipher = f.readlines()
                possible_shifts = find_shift_value(cipher[0])
                for i in possible_shifts:
                    print(check("".join(cipher),i))
        except FileNotFoundError:
            print("File Not Found.")
    else:
        print("Usage: python3 {} <cipher-file>".format(sys.argv[0]))
