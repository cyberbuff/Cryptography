import enchant
import string

class Validator:
    @staticmethod
    def is_sentence_valid(text):
        b = []
        dictionary = enchant.Dict("en_US")
        tempArray = text.split()
        for i in tempArray:
            b.append(dictionary.check(i))
        return (sum(b) > len(tempArray)/2)
    
    @staticmethod
    def has_nonprintable_characters(text):
        for char in text:
            if char not in string.printable:
                return True
        return False
    
    @staticmethod 
    def is_valid_word(word):
        dictionary = enchant.Dict("en_US")
        return dictionary.check(word)