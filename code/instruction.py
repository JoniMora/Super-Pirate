import pygame
from settings import screen_width, screen_height
from decoration import Bginstru

class Instru:
    def __init__(self, surface):

        self.display_surface = surface 
        self.bginstruction = Bginstru()

    def run(self):
        self.bginstruction.draw(self.display_surface)