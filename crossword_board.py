from typing import ClassVar
import numpy as np
from board_horse import board_horse
import random

class crossword_board(object):

    version = " Crossword Board 1.0 "
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self):
        self._version = crossword_board.version
        self.next_direction = crossword_board.HORIZONTAL
        self.X_max=20
        self.Y_max=20
        self.horses_on_board = set()
        self.board_array = np.zeros((self.X_max, self.Y_max), str)
        self.mask_horizontal = np.zeros((self.X_max, self.Y_max))
        self.mask_vertical = np.zeros((self.X_max, self.Y_max))
        
        # for i in range(self.X_max * self.Y_max):
        #     self.board_array.put(self.board_array,i,"M")

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

    def put (self, x,y, val):
        axis = x + y*self.X_max
        self.board_array.put(self.board_array,axis,val)

    def get_char (self, x,y):
        # axis = x + y*self.X_max
        return self.board_array[x,y]
        
    def get_next_direction(self):
        return self.next_direction

    def set_next_direction(self):
        if self.next_direction == crossword_board.HORIZONTAL:
            self.next_direction = crossword_board.VERTICAL
        else:
            self.next_direction = crossword_board.HORIZONTAL
        return self.next_direction

    @staticmethod
    def get_cross(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    #######################
    # Board 
    #######################

    def resize_board(self,x,y):
        self.board_array = np.resize (self.board_array,(x,y))
        #self.board_array.zeros( (x, y) , str)
        self.board_array.fill(" ")
        self.X_max=x
        self.Y_max=y

    def display (self):
        print(self.board_array)
        print("__________________")
        # print(self.mask_horizontal)
        # print(self.mask_vertical)

    #######################
    # Masking 
    #######################
    def mask_board(self, word, pos, direction):
        y=pos[0]
        x=pos[1]

        if direction == crossword_board.HORIZONTAL:
            i = 0 
            for char in list(word):
                self.mask_horizontal[y-1,x+i]=1
                self.mask_horizontal[y,x+i]=1
                self.mask_horizontal[y+1,x+i]=1
                i += 1

            self.mask_horizontal[y,x-1]=1
            self.mask_horizontal[y,x+len(word)]=1

            self.mask_horizontal[y-1,x-1]=0
            self.mask_horizontal[y+1,x-1]=0
            self.mask_horizontal[y-1,x+len(word)]=0
            self.mask_horizontal[y+1,x+len(word)]=0
        else:             
            i = 0 
            for char in list(word):
                self.mask_vertical[y+i,x-1]=1
                self.mask_vertical[y+i,x]=1
                self.mask_vertical[y+i,x+1]=1
                i += 1

            self.mask_vertical[y-1,x]=1
            self.mask_vertical[y+len(word),x]=1

            self.mask_vertical[y-1,x-1]=0
            self.mask_vertical[y-1,x+1]=0
            self.mask_vertical[y+len(word),x-1]=0
            self.mask_vertical[y+len(word),x+1]=0

    #######################
    # Placing a horse  
    #######################

    def draw_new_horse (self, word, pos, direction):
        y=pos[0]
        x=pos[1]
        i = 0 
        if direction == crossword_board.HORIZONTAL:
            for char in list(word):
                axis = (x + i) + y * self.X_max 
                np.put(self.board_array,axis,char)
                i += 1
        else:
            for char in list(word):
                axis = x + (y + i) * self.X_max
                np.put(self.board_array,axis,char)
                i += 1

    def place_horse_initial(self, word):
        pos = list()
        if self.next_direction == crossword_board.HORIZONTAL:
            x = int((self.X_max-len(word)) / 2)
            y = int(self.Y_max / 2)
            pos = (y,x)
        else:
            x = int(self.X_max / 2) 
            y = int((self.Y_max-len(word)) / 2)
            print(f"x={x}, y={y}")
            pos = (y,x)

        pos = self.place_new_horse(word, pos)
        
        return pos



    def position_new_horse(self, pick_word):
        
        # filtered_horses = filter(lambda horse: horse.direction ==  self.next_direction, self.horses_on_board)

        filtered_horses = list()
        item:board_horse
        for item in self.horses_on_board:
            if item.direction !=  self.next_direction:
                filtered_horses.append(item) 
        print(f"filtered: {list(filtered_horses)}")
        
        if len(filtered_horses) > 0:
            random_horse_on_board = random.choice(tuple(filtered_horses)) 
        else:
            random_horse_on_board = random.choice(tuple(self.horses_on_board)) 

        crossed_char_list = crossword_board.get_cross(random_horse_on_board.available_chars, pick_word)
        print (crossed_char_list)

        adjusted_axies = (0,0)

        if len(crossed_char_list) > 0: 
            cross_char = crossed_char_list[0]
            adjusted_axies = self.find_crossed_char_horse_axies(random_horse_on_board,cross_char)
            delta_index_pick = self.find_crossed_char_voca_index(pick_word, cross_char)

            print (f"-------------------------------------------")
            print (f"horse:             {random_horse_on_board}")
            print (f"horse_pos:         {random_horse_on_board.axis}")
            print (f"pick_word:         {pick_word}")
            print (f"crossed_spot:      {adjusted_axies}")
            print (f"delta              {delta_index_pick}")

            if self.next_direction == crossword_board.HORIZONTAL:
                adjusted_axies[1] = adjusted_axies[1] - delta_index_pick - 1
               
            else:
                adjusted_axies[0] = adjusted_axies[0] - delta_index_pick 

            print (f"adjusted           {adjusted_axies}")
            print (f"direction          {self.next_direction}")
            
        return adjusted_axies


    #####################
    # Handling Horse
    #####################
    def create_new_horse(self,voca, axies, direction):
        horse = board_horse(voca, axies, direction)
        self.horses_on_board.add(horse)

    def get_horse(self,voca):
        pass

    def list_horses(self):
        for i in self.horses_on_board:
            print (i) 

    def find_crossed_char_horse_axies(self,horse:board_horse,char):
        return horse.get_char_axies(char)

    def find_crossed_char_voca_index(self, voca, cross_char):
        index = list(voca).index(cross_char)
        return index 

    def place_new_horse (self, pick_word, pos):
        direction = self.get_next_direction()
        self.create_new_horse(pick_word, pos, direction)
        self.draw_new_horse (pick_word, pos, direction)
        self.mask_board(pick_word, pos, direction)     

        return pos

    def place_new_crossed_horse(self, pick_word):
        adjusted_axies = self.position_new_horse(pick_word)
        self.place_new_horse (pick_word, adjusted_axies)