from typing import ClassVar
import random

class gameplay(object):

    version = " vocaburary 1.0 "

    def __init__(self, board, words):
        self._version = gameplay.version
        self.board = board
        self.words = words

    def __repr__(self):
        return f'<gameplay> {format(self.version)}'

    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (gameplay.version.center(80, '='))
        return

    @staticmethod
    def printGuideline():
        print ("\t\t123456789012345678901234567890")
        return


    






