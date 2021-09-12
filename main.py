from vocaburary import vocaburary 
from crossword_board import crossword_board 

#############
# DRIVER
#############


def test_board(board):
    board.resize_board(16,16)
    board.put(0,0, "A")
    board.put(1,0, "B")
    board.put(0,1, "a")
    board.put(1,1, "b")
    board.put(15,15, "Z")
    board.display_board()
    board.print_version()
    return 

def test_voca(voca):
    
    word_list =  ["Melbourne", "Sydney", "School", "Brisbane", "Perth", "Norway", "Korea", "Amsterdam", "abcdefgabcdefg"]
    for word in word_list: 
        voca.word_collecton.add(word)

    print (voca.word_collecton)
    matched_chars = vocaburary.get_cross("abcdefgabcdefg", "giant")
    print (matched_chars)

    last_word = voca.get_word_randomly()
    voca.move_word_to_restroom(last_word)
    print (voca.word_collecton)
    print (voca.word_collecton_used)

    return 


wb = crossword_board()
myVoca = vocaburary()

test_board(wb)
test_voca(myVoca)
