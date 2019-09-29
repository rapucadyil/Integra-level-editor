import pygame

class Tile:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def __eq__(self, other):
        return (self.xpos == other.xpos) && (self.ypos == other.ypos) 

    def draw(self):
        pass