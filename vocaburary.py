from typing import ClassVar
import random
import csv

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
        self.word_collecton = random.sample(self.word_collecton, num_to_select)
        return 

    def get_word_randomly(self):
        return random.choice(tuple(self.word_collecton))
    
    def move_word_to_restroom(self, last_word):
        self.word_collecton.remove(last_word)
        return     

    def readCSV(self,filepath):
        with open(filepath, newline='\n') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            for row in datareader:
                self.add_word(row[0])


