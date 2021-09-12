from typing import ClassVar
import random

class vocaburary (object):

    version = " vocaburary 1.0 "

    def __init__(self):
        self._version = vocaburary.version
        self.word_collecton = set()
        self.word_collecton_used = set()
        #self.characters = list(self.word) # Split string to characters

    def __repr__(self):
        return f'<vocaburary> {format(self.version)}'

    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (vocaburary.version.center(80, '='))
        return

    @staticmethod
    def printGuideline():
        print ("\t\t123456789012345678901234567890")
        return

    @staticmethod
    def get_cross(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def add_word(self, word):
        self.word_collecton.add(word)
        return

    def get_word_randomly(self):
        return random.choice(tuple(self.word_collecton))
    
    def move_word_to_restroom(self, word):
        self.word_collecton.remove(word)
        self.word_collecton_used.add(word)
        return     

#############
# DRIVER
#############

vocaburary.print_version()
myVoca = vocaburary()

word_list =  ["Melbourne", "Sydney", "School", "Brisbane", "Perth", "Norway", "Korea", "Amsterdam", "abcdefgabcdefg"]

for word in word_list: 
    myVoca.word_collecton.add(word)

print (myVoca.word_collecton)

matched_chars = vocaburary.get_cross("abcdefgabcdefg", "giant")
print (matched_chars)

last_word = myVoca.get_word_randomly()
myVoca.move_word_to_restroom(last_word)
print (myVoca.word_collecton)
print (myVoca.word_collecton_used)



