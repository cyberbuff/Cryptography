import string
from enum import Enum

class FrequencyAnalyzer:
    @staticmethod
    def analyze_frequency(text):
        return {i:text.count(i) for i in string.ascii_lowercase}
    
    @staticmethod
    def calculate_frequency(text):
        return sum(filter(None,[XORFrequency.get((i).lower()) for i in text]))
    
    @staticmethod 
    def chisquaredstatistic(text):
        chi = (lambda x,y: ((x-y)**2)/y)
        text_length = len(text)
        return sum([chi(text.count(i),text_length*LetterFrequency[i].value) for i in string.ascii_lowercase])
    
    @staticmethod
    def findIC(text):
        """Determines the Index of Coincidence for the given text"""
        num = lambda x: x*(x-1)
        if len(text) == 1:
            return None
        else:
            ic_denominator = num(len(text))
            sum = 0
            for i in string.ascii_lowercase:
                sum += num(text.count(i))
            return (sum/ic_denominator)


class LetterFrequency(Enum):
    a = 0.0817
    b = 0.0149
    c = 0.0220
    d = 0.0425
    e = 0.1270
    f = 0.0223
    g = 0.0202
    h = 0.0609
    i = 0.0697
    j = 0.0015
    k = 0.0129
    l = 0.0403
    m = 0.0241
    n = 0.0675
    o = 0.0751
    p = 0.0193
    q = 0.0009
    r = 0.0599
    s = 0.0633
    t = 0.0936
    u = 0.0276
    v = 0.0098
    w = 0.0256
    x = 0.0015
    y = 0.0199
    z = 0.0008        

XORFrequency = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
} # TODO: Convert to enum with space
    

