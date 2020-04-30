import string
import itertools

def sort_dict_by_values(d2,reverse=False):
    d2 = dict(sorted(d2.items(), key=lambda x: x[1],reverse=reverse))
    return (list(d2.items()))

def process_text(text,case_insensitive=True):
    x = "".join([i for i in text if i in string.ascii_letters])
    if case_insensitive:
        return x.lower()
    return x
    
def hamming_distance(x, y):
    if isinstance(x,str):
        x = x.encode('ascii')
    if isinstance(y,str):
        y = y.encode('ascii')
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(len(x))])
    
    
    
def split_array(arr, number):
    a = [[] for _ in range(number)]
    x = (len(arr)//number)*number
    for i in range(x):
        a[i%number].append(arr[i])
    return a


def split_strings(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=" "))
    return ["".join(i) for i in transposedBlocks]