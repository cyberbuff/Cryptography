import string
import sys
import base64
from xor import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1],"r") as f:
                cipher = "".join(f.readlines())
                cipher = base64.b64decode(cipher)
                xor = XORCipher(cipher)
                result = xor.bruteforce()
                result.print()
        except FileNotFoundError:
            print("File Not Found.")
    else:
        print("Usage: python3 {} <cipher-file>".format(sys.argv[0]))