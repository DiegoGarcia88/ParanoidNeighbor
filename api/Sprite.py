import pygame
from api.GameObject import *
from api.CMath import *
    
class Sprite(GameObject):
    # Pivot types
    TOP_LEFT = 0
    CENTER = 1

    def __init__(self):
        GameObject.__init__(self)
        #Image(surface)
        self.mImg = None
        self.mWidth = 0
        self.mHeight = 0
        self.mVisible = True
        self.mRegistration = Sprite.TOP_LEFT
        self.mScore = 0

    def setScore(self,aScore):
        self.mScore = aScore

    def getScore(self):
        return self.mScore
    
    def setImage(self,aImgFile):
        self.mImg = aImgFile
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    def setRegistration(self, aRegistration):
        self.mRegistration = aRegistration

    def getImage(self):
        return self.mImg

    def update(self):
        GameObject.update(self)

    def render(self,aScreen):
        if (self.mImg != None):
            if (self.mVisible):
                img = self.mImg
                if (self.mRegistration == Sprite.TOP_LEFT):
                    aScreen.blit(img, (self.getX(), self.getY()))
                elif (self.mRegistration == Sprite.CENTER):
                    aScreen.blit(img, (self.getX() - self.getWidth() / 2, self.getY() - self.getHeight() / 2))

    def setVisible(self, aVisible):
        self.mVisible = aVisible

    def isVisible(self):
        return self.mVisible

    def getWidth(self):
        return self.mWidth

    def setWidth(self,aWidth):
        self.mWidth = aWidth

    def getHeight(self):
        return self.mHeight

    def setHeight(self, aHeight):
        self.mHeight = aHeight

    def setState(self,aState):
        GameObject.setState(self,aState)
        
    def collides(self,aSprite):
        x1 = self.getX()
        y1 = self.getY()
        w1 = self.getWidth()
        h1 = self.getHeight()
        x2 = aSprite.getX()
        y2 = aSprite.getY()
        w2 = aSprite.getWidth()
        h2 = aSprite.getHeight()
        return CMath.squareCollision(x1, y1, w1, h1, x2, y2, w2, h2)


        
    def destroy(self):
        self.mImg = None
        self.imgFileLeft = None
        self.imgFileRight = None
        
