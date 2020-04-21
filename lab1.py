import string
import sys
from caesar import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1],"r") as f:
                cipher = "".join(f.readlines())
                result = Caesar(cipher).bruteforce()
                result.print()
        except FileNotFoundError:
            print("File Not Found.")
    else:
        print("Usage: python3 {} <cipher-file>".format(sys.argv[0]))