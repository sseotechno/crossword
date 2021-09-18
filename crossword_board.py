from typing import ClassVar
import numpy as np
from board_horse import board_horse
from cross_checker import cross_checker
import random

class crossword_board(object):

    VERSION = " Crossword Board 1.0 "
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self):
        self._version = crossword_board.VERSION
        self.next_direction = crossword_board.HORIZONTAL
        self.X_max=20
        self.Y_max=20
        self.horses_on_board = set()
        self.board_array = np.zeros((self.X_max, self.Y_max), str)
        self.mask_horizontal = np.zeros((self.X_max, self.Y_max))
        self.mask_vertical = np.zeros((self.X_max, self.Y_max))
        self.cross_checker = cross_checker(self.X_max, self.Y_max)
        
        # for i in range(self.X_max * self.Y_max):
        #     self.board_array.put(self.board_array,i,"M")

    @property 
    def get_version(self):
        return self._version

    @staticmethod
    def print_version():
        print (crossword_board.VERSION.center(80, '='))
        return

    # def put (self, x,y, val):
    #     xy = x + y*self.X_max
    #     self.board_array.put(self.board_array,xy,val)

    def get_char (self, x,y):
        # xy = x + y*self.X_max
        return self.board_array[x,y]
        
    def get_next_direction(self):
        return self.next_direction

    def set_next_direction(self):
        if self.next_direction == crossword_board.HORIZONTAL:
            self.next_direction = crossword_board.VERTICAL
        else:
            self.next_direction = crossword_board.HORIZONTAL
        return self.next_direction

    #######################
    # Board 
    #######################

    def resize_board(self,x,y):
        self.board_array = np.resize (self.board_array,(x,y))
        self.board_array.fill(" ")
        self.X_max=x
        self.Y_max=y

    def display (self):
        print(self.board_array)
        print("__________________")
 
    #######################
    # Placing a horse  
    #######################

    def place_horse_initial(self, word):
        pos = list()
        if self.next_direction == crossword_board.HORIZONTAL:
            x = int((self.X_max+len(word)) / 2 - len(word))
            y = int(self.Y_max / 2)
            pos = (y,x)
        else:
            x = int(self.X_max / 2) 
            y = int((self.Y_max+len(word)) / 2 - len(word))
            pos = (y,x)

        print(f"x={x}, y={y}")        
        pos = self.place_new_horse(word, pos)
        
        return pos

    def positioning_horse(self, new_word):
        
        new_xy=(0,0)

        # filtered_horses = filter(lambda horse: horse.direction ==  self.next_direction, self.horses_on_board)
        horses_located_in_cross_lines = list()
        item:board_horse
        for item in self.horses_on_board:
            if item.direction !=  self.next_direction:
                horses_located_in_cross_lines.append(item) 

        print(f"Filtered: {list(horses_located_in_cross_lines)}")
        
        crossed_char_list=list()
        if len(horses_located_in_cross_lines) > 0:
            a_random_horse_in_cross_lines = random.choice(tuple(horses_located_in_cross_lines)) 
            crossed_char_list = cross_checker.find_matched_chars(a_random_horse_in_cross_lines.available_chars, new_word)

        if len(crossed_char_list) > 0: 
            cross_char = random.choice(tuple(crossed_char_list))
            new_xy = self.find_crossed_char_horse_xy(a_random_horse_in_cross_lines,cross_char)
            delta = cross_checker.find_index_char_from_word(new_word, cross_char)
            if self.next_direction == crossword_board.HORIZONTAL:
                new_xy[1] = new_xy[1] - delta - 1
            else:
                new_xy[0] = new_xy[0] - delta 

            print (f"-------------------------------------------")
            print (f"crosssed char(s):  {crossed_char_list}")
            print (f"horse:             {a_random_horse_in_cross_lines}")
            print (f"horse_pos:         {a_random_horse_in_cross_lines.xy}")
            print (f"new_word:          {new_word}")
            print (f"crossed_spot:      {new_xy}")
            print (f"delta              {delta}")
            print (f"direction          {self.next_direction}")
                
            if (new_xy[0] < 0 or new_xy[1] < 0): 
                return (0,0)

        return new_xy
    
    def draw_new_horse (self, word, pos, direction):
        y=pos[0]
        x=pos[1]
        i = 0 
        if direction == crossword_board.HORIZONTAL:
            for char in list(word):
                xy = (x + i) + y * self.X_max 
                np.put(self.board_array,xy,char)
                i += 1
        else:
            for char in list(word):
                xy = x + (y + i) * self.X_max
                np.put(self.board_array,xy,char)
                i += 1

    def find_crossed_char_horse_xy(self,horse:board_horse,char):
        return horse.get_1st_char_xy(char)


    #####################
    # Handling Horse
    #####################
    def create_new_horse(self,voca, xy, direction):
        horse = board_horse(voca, xy, direction)
        self.horses_on_board.add(horse)

    def get_horse(self,voca):
        pass

    def list_horses(self):
        for i in self.horses_on_board:
            print (i) 

    #################
    # PLACE NEW HORSE
    def place_new_horse (self, new_word, pos):
        direction = self.get_next_direction()

        if self.cross_checker.check_boundary(new_word, pos, direction):
            self.cross_checker.mark_new_cells(new_word, pos, direction)
            if self.cross_checker.comparison_in_same_direction(direction):
                self.create_new_horse(new_word, pos, direction)
                self.draw_new_horse (new_word, pos, direction)
                self.cross_checker.mark_used_cells(new_word, pos, direction)
        # self.mask_board(new_word, pos, direction)     

        return pos

    def place_new_crossed_horse(self, new_word):
        new_xy = self.positioning_horse(new_word)
        print (f"New horse positon = {new_xy}")
        self.place_new_horse (new_word, new_xy)