from typing import ClassVar

class board_horse(object):

    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self, voca, yx:list, direction):
        self.word = voca 
        self.yx = yx
        self.direction = direction
        self.crossed_words_count = 0
        self.available_chars = list(voca)

    def __repr__(self):
        return f'<board_horse> ({self.yx}) {self.direction} : {self.word} '
    
    def remove_available_char(self,char):
        self.available_chars.remove(char)

    def get_1st_char_yx(self,char):
        ''' return yx of char location '''
        index = list(self.word).index(char)
        yx = list(self.yx)
        
        print (f"char index: {char} {index}")
        print (f"horse.yx {self.yx[0]} {self.yx[1]}")

        if self.direction == board_horse.HORIZONTAL:
            yx[1]=self.yx[1]+index
        else:
            yx[0]=self.yx[0]+index
        
        return yx
            

