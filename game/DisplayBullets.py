from api.Sprite import *
import pygame



class DisplayBullets(Sprite):
    EMPTY = 0
    ONE_BULLET = 1
    TWO_BULLETS = 2
    INFINITE = 3

    def __init__(self):
        Sprite.__init__(self)
        self.setState(DisplayBullets.TWO_BULLETS)
        self.mBullets = 2



    def setState(self,aState):
        Sprite.setState(self, aState)
        if(self.getState() == DisplayBullets.EMPTY):
            img = pygame.image.load("assets/images/Bullet00.png")
            self.setImage(img)
        if (self.getState() == DisplayBullets.ONE_BULLET):
            img = pygame.image.load("assets/images/Bullet01.png")
            self.setImage(img)
        if (self.getState() == DisplayBullets.TWO_BULLETS):
            img = pygame.image.load("assets/images/Bullet02.png")
            self.setImage(img)
        if (self.getState() == DisplayBullets.INFINITE):
            img = pygame.image.load("assets/images/IBox00.png")
            self.setImage(img)

    def setBullets(self,aBullets):
        self.mBullets = aBullets

    def update(self):
        Sprite.update(self)
        if(self.mBullets == 0):
            self.setState(DisplayBullets.EMPTY)
        if (self.mBullets == 1):
            self.setState(DisplayBullets.ONE_BULLET)
        if (self.mBullets == 2):
            self.setState(DisplayBullets.TWO_BULLETS)
        if (self.mBullets > 2):
            self.setState(DisplayBullets.INFINITE)

    def render(self, aScreen):
        Sprite.render(self, aScreen)

    def destroy(self):
        Sprite.destroy()
