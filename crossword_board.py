from typing import ClassVar
import numpy as np


class crossword_board(object):

    version = " Crossword Board 1.0 "

    def __init__(self):
        self._version = crossword_board.version
        self._masterDict = dict()
        self._dialedDict = dict()
        self._ascii_list = list()
        self._indexList = list()
        self.X_max=18
        self.Y_max=18
        self.board_array = np.zeros((self.X_max, self.Y_max), str)

    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (crossword_board.version.center(80, '='))
        return

    @staticmethod
    def printGuideline():
        print ("\t\t123456789012345678901234567890")
        return

    def resize_board(self,x,y):
        self.board_array = np.resize (self.board_array,(x,y))
        self.board_array = np.zeros( (x, y) , str)
        self.X_max=x
        self.Y_max=y


    def display_board(self):
        print(self.board_array)

    def put (self, x,y, val):

        axis = x + y*self.X_max
        np.put(self.board_array,axis,val)
