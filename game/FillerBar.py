import pygame
from api.Sprite import *

class FillerBar(Sprite):

    def __init__(self,aImg):
        Sprite.__init__(self)
        image = pygame.image.load(aImg)
        image = image.convert()
        self.setImage(image)


    def update(self):
        Sprite.update(self)
        
    def render(self,aScreen):
        Sprite.render(self, aScreen)

    def destroy(self):
        Sprite.destroy(self)
