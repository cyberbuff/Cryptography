from utils import *
import base64
from statistics import mean
from xor import *
import itertools


def normalized_edit_distance(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)][0:4]
    pairs = list(itertools.combinations(blocks, 2))
    scores = [hamming_distance(p[0], p[1])/float(k) for p in pairs][0:4]
    return mean(scores)


def break_repeating_xor(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [XORCipher(i).bruteforce().key for i in transposedBlocks]
    return bytes(key)


with open("part4.txt","r") as f:
    cipher_text = f.read()
    cipher_text = base64.b64decode(cipher_text)
    key_length = min(range(2, 50), key=lambda k: normalized_edit_distance(cipher_text, k))
    cipher_key = break_repeating_xor(cipher_text,key_length)
    print(XORCipher.decode(cipher_text,cipher_key))