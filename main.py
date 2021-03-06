from vocaburary import vocaburary 
from crossword_board import crossword_board 
from gameplay import gameplay 
import numpy
import random
# import os

from os import system

#############
# DRIVER
#############

def test_board(board):
    board.print_version()
    board.resize_board(30,30)
    board.put(0,0, "A")
    board.put(1,0, "B")
    board.put(0,1, "a")
    board.put(1,1, "b")
    board.put(15,15, "Z")
    board.display_board()
    return 

def test_voca(voca):
    word_list =  ["Melbourne", "Sydney", "School", "Brisbane", "Perth", "Norway", "Korea", "Amsterdam", "abcdefgabcdefg"]
    for item in word_list: 
        pass
        # voca        .word_collecton.add(item)

    matched_chars = vocaburary.get_cross("abcdefgabcdefg", "giant")
    print (matched_chars)
    return 

if __name__ == "__main__":


    print (f"==============================================================")
    print (f"===========================START==============================")
    print (f"==============================================================")

    ## AJUST WIDTH OF TERMINAL 
    # system('mode con cols=120')
    numpy.set_printoptions(linewidth=160)



    #####################
    # PARAMETERS 
    #####################
    VOCA_COUNT = 30
    WORD_COUNT = 30
    BOARD_SIZE = 30
    FILE_NAME = 'countries.csv'

    #####################
    # RUN  
    #####################

    cb = crossword_board(BOARD_SIZE,BOARD_SIZE)
    cb.resize_board(BOARD_SIZE,BOARD_SIZE)
    myVoca = vocaburary()
    myVoca.readCSV(FILE_NAME)
    myVoca.select_final_list_randomly(VOCA_COUNT)
    game = gameplay(cb,myVoca)

    #test_board(cb)
    test_voca(myVoca)

    new_word = myVoca.get_word_randomly()
    cb.place_horse_initial(new_word)
    myVoca.move_word_to_restroom(new_word)
    cb.set_next_direction()
    cb.display()

    while WORD_COUNT > 0:     
        if len(myVoca.word_collecton) > 0: 
            new_word = myVoca.get_word_randomly()
            cb.place_new_crossed_horse(new_word)
            myVoca.move_word_to_restroom(new_word)
            cb.display()
            cb.set_next_direction()            
            WORD_COUNT -= 1
        else:
            WORD_COUNT = 0 

    cb.list_horses()
    cb.get_random_location(new_word)




    




