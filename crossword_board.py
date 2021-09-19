from typing import ClassVar
import numpy as np
from word_horse import word_horse
from cross_checker import cross_checker
import random

class crossword_board(object):

    VERSION = " Crossword Board 1.0 "
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self,x,y):
        self._version = crossword_board.VERSION
        self.next_direction = crossword_board.HORIZONTAL
        self.X_max=x
        self.Y_max=y
        self.horses_on_board = set()
        self.board_array = np.zeros((self.X_max, self.Y_max), str)
        self.mask_horizontal = np.zeros((self.X_max, self.Y_max))
        self.mask_vertical = np.zeros((self.X_max, self.Y_max))
        self.cross_checker = cross_checker(self.X_max, self.Y_max)

        self.CROSS_CHECK_RETRY_COUNT = 30        # RETRY COUNTER - checking count of new corssed words 
        self.RANDOM_POSITION_RETRY_COUNT = 20    # RETRY COUNTER - checking identifying avaialble cell randomly 

        
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
    #     yx = x + y*self.X_max
    #     self.board_array.put(self.board_array,yx,val)

    def get_char (self, x,y):
        # yx = x + y*self.X_max
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

    def determin_1st_horse_pos(self, new_word):
        pos = list()
        if self.next_direction == crossword_board.HORIZONTAL:
            x = int((self.X_max+len(new_word)) / 2 - len(new_word))
            y = int(self.Y_max / 2)
            pos = (y,x)
        else:
            x = int(self.X_max / 2) 
            y = int((self.Y_max+len(new_word)) / 2 - len(new_word))
            pos = (y,x)
        return pos


    def determine_horse_pos_crossed(self, new_word, random_pos=False):
        new_yx=tuple((0,0))

        # filtered_horses = filter(lambda horse: horse.direction ==  self.next_direction, self.horses_on_board)
        horses_in_same_direction = list()
        item:word_horse
        for item in self.horses_on_board:
            if item.direction !=  self.next_direction:
                horses_in_same_direction.append(item) 
        
        if len(horses_in_same_direction) > 0:
            np.random.seed()
            random.shuffle(horses_in_same_direction)
            
            a_random_horse_in_cross_lines = random.choice(tuple(horses_in_same_direction)) 
            crossed_char_list = list()
            crossed_char_list = cross_checker.find_matched_chars(a_random_horse_in_cross_lines.available_chars, new_word)
    
            if (len(crossed_char_list) == 0 ):
                return (0,0)

            cross_char = random.choice(tuple(crossed_char_list))
            crosssed_yx = self.find_crossed_char_yx(a_random_horse_in_cross_lines,cross_char)
            
            delta = cross_checker.find_index_char_from_word(new_word, cross_char)
            if self.next_direction == crossword_board.HORIZONTAL:
                new_yx = tuple((crosssed_yx[0], crosssed_yx[1] - delta))
            else:
                new_yx = tuple((crosssed_yx[0] - delta, crosssed_yx[1]))
            
            print (f"Crossed horse:     {a_random_horse_in_cross_lines}")
            print (f"horse_pos:         {a_random_horse_in_cross_lines.yx}")
            print (f"crosssed char(s):  {crossed_char_list}")
            print (f"direction          {self.next_direction}")
            print (f"new_word:          {new_word}")
            print (f"new_yx:            {new_yx}")
            print (f"delta              {delta}")
            

        print (f"final new_yx: {new_yx}")
        return new_yx

    def determine_horse_pos_randomly (self, new_word, direction, retry_count=10): 
        print (f">>>>>>>>>>>>> NEW POSITION IS REQUIRED (RANDOM)")
        print (f">>>>>>>>>>>>>{new_word}")
        
        found_valid_random_spot = False
        while found_valid_random_spot == False and retry_count > 0: 
            response = self.get_random_location(new_word)
            found_valid_random_spot = response[0] #Identify valid position for new word (not crossed)
            new_yx = response[1]
            retry_count -= 1
        
        print (f"final new_yx: {new_yx}")

        if retry_count == 0: 
            return (0,0)
        else:
            return new_yx


    def draw_new_horse (self, new_word, pos, direction):
        y=pos[0]
        x=pos[1]
        i = 0 
        if direction == crossword_board.HORIZONTAL:
            for char in list(new_word):
                #yx = (x + i) + y * self.X_max 
                #np.put(self.board_array,yx,char)
                self.board_array[y,x + i]=char 
                i += 1
        else:
            for char in list(new_word):
                #yx = x + (y + i) * self.X_max
                #np.put(self.board_array,yx,char)
                self.board_array[y+i,x]=char 
                i += 1
        self.cross_checker.mark_used_cells(new_word, pos, direction)

    def find_crossed_char_yx(self,horse:word_horse,char):
        return horse.get_available_char_yx(char)

    #####################
    # Handling Horse
    #####################
    
    def get_horse(self,voca):
        pass

    def list_horses(self):
        for i in self.horses_on_board:
            print (i) 

    #################
    # VALIDATE THE NEW POSITION 

    def __validate_new_position (self, new_word, pos, direction):

        if not self.cross_checker.check_word_length(new_word, self.X_max,self.Y_max):
            return False 

        if not self.cross_checker.check_boundary(new_word, pos, direction):
            return False

        self.cross_checker.mark_new_cells(new_word, pos, direction)

        if not self.cross_checker.comparison_in_same_direction(direction):
            return False

        if not cross_checker.check_individual_char_in_cells(self.board_array, new_word, pos, direction):
            return False 
            
        return True 

    #################
    # PLACE NEW HORSE
    def __place_new_horse (self, new_word, pos):
        
        direction = self.get_next_direction()

        while (not self.__validate_new_position(new_word, pos, direction)) and self.CROSS_CHECK_RETRY_COUNT > 0:
            pos = self.determine_horse_pos_crossed(new_word) 
            self.CROSS_CHECK_RETRY_COUNT -= 1

        #IF NO CROSSED WORD is FOUND, go RANDOM LOCATION
        if self.CROSS_CHECK_RETRY_COUNT == 0:
            pos = self.determine_horse_pos_randomly(new_word,direction, retry_count = self.RANDOM_POSITION_RETRY_COUNT)
            if pos == (0,0):
                return (0,0)

        if self.__validate_new_position(new_word, pos, direction):                 
            self.cross_checker.mark_new_cells(new_word, pos, direction)
            # CREATE A NEW HORSE 
            horse = word_horse(new_word, pos, direction)
            self.horses_on_board.add(horse)
            self.draw_new_horse (new_word, pos, direction)
            return pos
        else: 
            return (0,0)

    def place_horse_initial(self,new_word):
        new_yx = self.determin_1st_horse_pos(new_word)
        self.__place_new_horse (new_word, new_yx)

    def place_new_crossed_horse(self, new_word):
        new_yx = self.determine_horse_pos_crossed(new_word)        
        self.__place_new_horse (new_word, new_yx)

    def get_random_location(self,new_word):
        outcome = self.cross_checker.get_random_valid_pos(self.next_direction, new_word)
        return outcome



