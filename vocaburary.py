from typing import ClassVar
import random
import csv
from random import shuffle

class vocaburary (object):

    VERSION = " vocaburary 1.0 "

    def __init__(self):
        self._version = vocaburary.VERSION
        self.word_collecton = set()
        self.word_collecton_used = set()
        #self.characters = list(self.word) # Split string to characters

    def __repr__(self):
        return f'<vocaburary> {format(self.VERSION)}'
        
    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (vocaburary.VERSION.center(80, '='))
        return

    @staticmethod
    def get_cross(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def add_word(self, word):
        self.word_collecton.add(word)
        return

    def select_final_list_randomly(self, num_to_select):
        random.seed()
        self.word_collecton = random.sample(self.word_collecton, num_to_select)
        return 

    def get_word_randomly(self):
        print (f"get_word_randomly:  {len(self.word_collecton)}")
        if (len(self.word_collecton) > 0):
            random.seed()
            return random.choice(tuple(self.word_collecton))
    
    def move_word_to_restroom(self, last_word):

        if (len(self.word_collecton) > 0):
            self.word_collecton.remove(last_word)

        print (f"LEFT word count in collection = {len(self.word_collecton)}")
        return     

    def readCSV(self,filepath):
        with open(filepath, newline='\n') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            for row in datareader:
                self.add_word(row[0])


