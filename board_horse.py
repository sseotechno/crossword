from typing import ClassVar

class board_horse(object):

    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __init__(self, voca, xy:list, direction):
        self.word = voca 
        self.xy = xy
        self.direction = direction
        self.crossed_words_count = 0
        self.available_chars = list(voca)

    def __repr__(self):
        return f'<board_horse> ({self.xy}) {self.direction} : {self.word} '
    
    def remove_available_char(self,char):
        self.available_chars.remove(char)

    def get_1st_char_xy(self,char):
        ''' return xy of char location '''
        index = list(self.word).index(char)
        xy = list(self.xy)
        
        print (f"char index: {char} {index}")
        print (f"horse.xy {self.xy[0]} {self.xy[1]}")

        if self.direction == board_horse.HORIZONTAL:
            xy[1]=self.xy[1]+index
        else:
            xy[0]=self.xy[0]+index
        
        return xy
            

