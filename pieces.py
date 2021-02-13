import pygame

class pieces(object):

    def __init__(self, imagePath, posx, posy, colour, value, name):
        self.img = pygame.image.load(imagePath)
        self.posx, self.posy = posx, posy
        self.colour = colour.lower()
        self.value = value
        self.name = name.lower()

        self.arrayPosx, self.arrayPosy = self.findArray()

    def check(self):
        pass
    
    def findArray(self):
        return int((self.posx-100)/100), int((self.posy-46)/100)