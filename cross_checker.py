from typing import ClassVar
import numpy as np
from board_horse import board_horse
import random

class cross_checker(object):
    
    VERSION = " Cross Checker 1.0 "
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self, x, y):
        self._version = cross_checker.VERSION
        self.next_direction = cross_checker.HORIZONTAL
        self.X_max=x
        self.Y_max=y
        
        self.board_new_horse = np.zeros((self.X_max, self.Y_max), dtype = bool)
        self.board_used_cells = np.zeros((self.X_max, self.Y_max), dtype = bool)
        self.mask_horizontal = np.zeros((self.X_max, self.Y_max),dtype = bool)
        self.mask_vertical = np.zeros((self.X_max, self.Y_max),dtype = bool)
    
    # for i in range(self.X_max * self.Y_max):
    #     self.board_array.put(self.board_array,i,"M")

    # def put (self, x,y, val):
    #     axis = x + y*self.X_max
    #     self.board_used_cells.put(self.board_used_cells,axis,val)

    def mark_used_cells (self, word, pos, direction):
        y=pos[0]
        x=pos[1]
        i = 0 
        if direction == cross_checker.HORIZONTAL:
            for char in list(word):
                self.mask_horizontal[y,x + i]=1
                i += 1
            self.mask_board(word, x, y, direction)
        else:
            for char in list(word):
                self.mask_vertical[y+i,x]=1
                i += 1
            self.mask_board(word, x, y, direction)
   
    def mark_new_cells (self, word, pos, direction):
        self.reset_new_cell_aray()
        y=pos[0]
        x=pos[1]
        i = 0 
        if direction == cross_checker.HORIZONTAL:
            for char in list(word):
                self.board_new_horse[y,x+i]=1
                i += 1
        else:
            for char in list(word):
                self.board_new_horse[y+i,x]=1
                i += 1

    def reset_new_cell_aray(self):
        self.board_new_horse = np.zeros((self.X_max, self.Y_max), dtype = bool)

    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (cross_checker.VERSION.center(80, '='))
        return

    @staticmethod
    def printGuideline():
        print ("\t\t123456789012345678901234567890")
        return

    @staticmethod
    def find_matched_chars(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    @staticmethod
    def find_index_char_from_word(voca, cross_char):
        index = list(voca).index(cross_char)
        return index 

    def mask_new_horse (self, new_word, pos, direstion):
        self.mask_board(new_word, pos, direstion)  

    #######################
    # Masking 
    #######################
    def mask_board(self, word, x,y , direction):

        if direction == cross_checker.HORIZONTAL:
            i = 0 
            for char in list(word):
                if (y-1 >= 0 and x+i < self.X_max): 
                    self.mask_horizontal[y-1,x+i]=1
                if (x+i < self.X_max): 
                    self.mask_horizontal[y,x+i]=1
                if (y+1 < self.Y_max and x+i < self.X_max): 
                    self.mask_horizontal[y+1,x+i]=1
                i += 1

            if (x-1 >= 0): 
                self.mask_horizontal[y,x-1]=1

            if (x+len(word) < self.X_max): 
                self.mask_horizontal[y,x+len(word)]=1

            if y-1 >= 0:
                if x-1 >= 0: 
                    self.mask_horizontal[y-1,x-1]=0
                if x+len(word) < self.X_max: 
                    self.mask_horizontal[y-1,x+len(word)]=0

            if y+1 < self.Y_max: 
                if x-1 >= 0: 
                    self.mask_horizontal[y+1,x-1]=0
                if x+len(word) < self.X_max: 
                    self.mask_horizontal[y+1,x+len(word)]=0
        else:             
            i = 0 
            for char in list(word):
                if (y+1 < self.Y_max and x-1 >= 0): 
                    self.mask_vertical[y+i,x-1]=1
                if (y+1 < self.Y_max): 
                    self.mask_vertical[y+i,x]=1
                if (y+1 < self.Y_max and x+1 < self.X_max): 
                    self.mask_vertical[y+i,x+1]=1
                i += 1

            if (y-1 >= 0): 
                self.mask_vertical[y-1,x]=1
            
            if (y+len(word) < self.Y_max): 
                self.mask_vertical[y+len(word),x]=1

            if y-1 >= 0:
                if x-1 >= 0: 
                    self.mask_vertical[y-1,x-1]=0
                if x+1 < self.X_max: 
                    self.mask_vertical[y-1,x+1]=0

            if y+len(word) < self.Y_max:
                if x-1 > 0: 
                    self.mask_vertical[y+len(word),x-1]=0
                if x+1 < self.X_max: 
                    self.mask_vertical[y+len(word),x+1]=0


    def __compare_arrays_overlay(self, array1, array2):        
        result = False 
        tempArray = np.logical_and(array1,array2)
        if np.count_nonzero(tempArray == True) == 0 : # IF NO EXISTING CELL IS OVERWRITTEN
            result = True
        else:
            result = False
        return result 

    def comparison_in_same_direction(self, direction):
        
        if direction == cross_checker.HORIZONTAL:
            result = self.__compare_arrays_overlay(self.mask_horizontal,self.board_new_horse)
        else:
            result = self.__compare_arrays_overlay(self.mask_vertical,self.board_new_horse)
        return result 

    def check_boundary(self, word, pos, direction):
        y=pos[0]
        x=pos[1]
        result = True 

        if direction == cross_checker.HORIZONTAL:
            if (x + len(word) >= self.X_max): 
                result = False 
        else: 
            if (y + len(word) >= self.Y_max): 
                result = False

            print (f'check_bound - ({x}, {y})')

        return result

    def get_random_valid_pos(self, direction, new_word):
        result = False
        tempArray = np.zeros((self.X_max, self.Y_max), dtype = bool)
        
        if direction == cross_checker.HORIZONTAL:
            random_num_X = np.random.randint(0,self.X_max-len(new_word))
            random_num_Y = np.random.randint(0,self.Y_max)
            # print (f"WORD:      {new_word}")
            # print (f"RANDOM: X: {random_num_X}")
            # print (f"RANDOM: Y: {random_num_Y}")
            i = 0 
            for char in list(new_word):
                yx = (random_num_X + i) + random_num_Y * self.X_max 
                np.put(tempArray,yx,char)
                i += 1
            result = self.__compare_arrays_overlay(tempArray, self.mask_horizontal)
        else:
            random_num_X = np.random.randint(0,self.X_max)

            # print (f"new_word+1:                      {new_word}")
            # print (f"self.Y_max-len(new_word)+1:      {self.Y_max-len(new_word)}")

            random_num_Y = np.random.randint(0,self.Y_max-len(new_word)+1)
            
            # print (f"WORD:      {new_word}")
            # print (f"RANDOM: X: {random_num_X}")
            # print (f"RANDOM: Y: {random_num_Y}")
            i = 0 
            for char in list(new_word):
                tempArray[random_num_Y + i, random_num_X] = char 
                i += 1
            result = self.__compare_arrays_overlay(tempArray, self.mask_vertical)

        return (result, (random_num_Y, random_num_X))


    def check_individual_char_in_cells(board_array, word, start_pos, direction):
            result = True
            y=start_pos[0]
            x=start_pos[1]
            i = 0 
            if direction == cross_checker.HORIZONTAL:
                for char in list(word):
                    cell_value = board_array[y,x+i]
                    if (char != cell_value and cell_value  !=" "):
                        result = False 
                    i += 1
            else:
                for char in list(word):
                    cell_value = board_array[y+i,x]
                    if (char != cell_value and cell_value  !=" "):
                        result = False 
                    i += 1
            return result