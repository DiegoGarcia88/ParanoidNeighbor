import random
import pygame
from api.GameObject import *
from api.GameConstants import *
from api.Sprite import *
#TODO: change this into a manager
class Clouds(GameObject):

    def __init__(self,aSPEED, aCLOUD_COUNT):
        GameObject.__init__(self)
        self.mCLOUD_COUNT = aCLOUD_COUNT
        self.mSPEED = aSPEED
        self.mWidth = GameConstants.inst().SCREEN_WIDTH
        self.mHeight = GameConstants.inst().SCREEN_HEIGHT
        self.mCloudList = []
        self.mClouds = []
        # Randomly create the original set of stars
        for i in range(aCLOUD_COUNT):
            self.mCloudList.append([self.mWidth + i*2500, random.randrange(0, self.mHeight / 2)])
        i = 0
        while(i < 2):
            cloud = Sprite()
            tmpImg = pygame.image.load("assets\images\Cloud0" + str(i) + ".png")
            tmpImg = tmpImg.convert_alpha()
            cloud.setImage(tmpImg)
            cloud.setVelX(aSPEED)
            cloud.setXY(self.mCloudList[i][0],self.mCloudList[i][1])
            self.mClouds.append(cloud)
            i += 1

            
                            
    def update(self):
        i = 0
        while(i < 2):
            self.mClouds[i].update()
            #If Clouds Go Left of the screen
            if (self.mClouds[i].getX() < 0 - self.mClouds[i].getWidth()):
                self.mClouds[i].setX(self.mWidth)
                self.mClouds[i].setY(random.randrange(0, self.mHeight / 2))
            i += 1


    def render(self, aScreen):
        i = 0
        while (i < 2):
            self.mClouds[i].render(aScreen)
            i += 1


    def destroy(self):
        GameObject.destroy(self)