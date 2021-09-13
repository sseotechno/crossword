from typing import ClassVar

class board_horse(object):

    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self, voca, axis:list, direction):
        self.word = voca 
        self.axis = axis
        self.direction = direction
        self.crossed_words_count = 0
        self.available_chars = list(voca)

    def __repr__(self):
        return f'<board_horse> ({self.axis}) {self.direction} : {self.word} '
    
    def remove_available_char(self,char):
        self.available_chars.remove(char)

    def get_char_axies(self,char):
        ''' return axies of char location '''
        index = list(self.word).index(char)
        axis = list(self.axis)
        
        print (f"char index: {char} {index}")
        print (f"horse.axis {self.axis[0]} {self.axis[1]}")

        if self.direction == board_horse.HORIZONTAL:
            axis[1]=self.axis[1]+index
        else:
            axis[0]=self.axis[0]+index
        
        return axis
            

