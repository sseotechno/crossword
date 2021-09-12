from vocaburary import vocaburary 
from crossword_board import crossword_board 

#############
# DRIVER
#############

wb = crossword_board()

wb.resize_board(16,16)
wb.put(0,0, "A")
wb.put(1,0, "B")
wb.put(0,1, "a")
wb.put(1,1, "b")
wb.put(15,15, "Z")
wb.display_board()

wb.print_version()


myVoca = vocaburary()

word_list =  ["Melbourne", "Sydney", "School", "Brisbane", "Perth", "Norway", "Korea", "Amsterdam", "abcdefgabcdefg"]

for word in word_list: 
    myVoca.word_collecton.add(word)

print (myVoca.word_collecton)

matched_chars = vocaburary.get_cross("abcdefgabcdefg", "giant")
print (matched_chars)

last_word = myVoca.get_word_randomly()
myVoca.move_word_to_restroom(last_word)
print (myVoca.word_collecton)
print (myVoca.word_collecton_used)

