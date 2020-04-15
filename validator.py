import enchant
import string

class Validator:
    def __init__(self):
        super().__init__()


    def is_sentence_valid(self, text):
        b = []
        dictionary = enchant.Dict("en_US")
        tempArray = text.split()
        for i in tempArray:
            b.append(dictionary.check(i))
        return (sum(b) > len(tempArray)/2)    
    
    
    def has_nonprintable_characters(self, text):
        for char in text:
            if char not in string.printable:
                return True
        return False
    
    
    def check(self, text):
        if (self.has_nonprintable_characters(text)):
            return False
        if self.is_sentence_valid(text):
            return True
        return False