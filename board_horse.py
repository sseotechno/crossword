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
        self.indexed_char_list = board_horse.create_indexed_char_list(voca)

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

    def get_available_char_yx(self,char):
        ''' return yx of available char location '''

        inedx = 0 
        for (i, available_char) in self.indexed_char_list:
            if  available_char == char: 
                index = i

        yx = list(self.yx)

        if self.direction == board_horse.HORIZONTAL:
            yx[1]=self.yx[1]+index
        else:
            yx[0]=self.yx[0]+index
        
        return yx

    @staticmethod
    def create_indexed_char_list(voca):    
        indexed_chars_list = list()
        i = 1
        for char in tuple(voca):
            indexed_chars_list.append ((i,char))
            i += 1
        return indexed_chars_list



