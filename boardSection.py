class board(object):

    def __init__(self, colour, posx, posy):

        self.colour = colour
        self.posx = posx
        self.posy = posy

        self.arrayPosx, self.arrayPosy = self.findArray()
        

    def findArray(self):
        return int((self.posx-100)/100), int((self.posy-46)/100)

