import pygame
import random
import math
from api.CMath import *
from api.AnimatedSprite import *
from api.GameConstants import *
from game.EnemyManager import *
from api.AudioManager import *
from game.GameData import *
from game.Pickup import *

class Enemy(AnimatedSprite):
    #State machine
    START = 0
    NORMAL = 1
    EXPLODING = 2
    EXITING = 3
    FADE_TIME = 45
    LIFE_TIME = 300

    def __init__(self):
        AnimatedSprite.__init__(self)
        self.mFrames = []
        self.mOrbitCenter = []
        self.mDistance = 300
        self.mTimeAtSameSpeed = 0
        self.mTimeAlive = 0
        self.mMaxTimeAtSameSpeed = 60
        self.mScaleWidth = 0
        self.mScaleHeight = 0
        name = "assets/images/Drone0"
        self.setScore(10)
        #Load Image sequence
        self.mFramesNormal = []
        self.setRegistration(Sprite.CENTER)
        i = 0
        while(i <= 6):
            tmpImg = pygame.image.load(name + str(i) + ".png")
            tmpImg = tmpImg.convert_alpha()
            #After changing from place holders to final art the drones(same size) look smaller so I am scaling them up 1.5x
            tmpImg = pygame.transform.scale(tmpImg, (114, 51))
            self.mFramesNormal.append(tmpImg)
            i += 1
        self.mFadeTime = 0
        self.mFramesFadeIn = []
        self.mFramesFadeOut = []
        i = 0
        width = 0
        height = 0
        #TODO: change 76 and 34 from fixed values to original image width and heightf
        while (i < Enemy.FADE_TIME):
            tmpImg = pygame.image.load(name + str(0) + ".png")
            tmpImg = tmpImg.convert_alpha()
            width = width + 76 / Enemy.FADE_TIME
            height = height + 34 / Enemy.FADE_TIME
            tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
            self.mFramesFadeIn.append(tmpImg)
            i += 1
        i = Enemy.FADE_TIME
        width = 76
        height = 34
        while (i > 0):
            tmpImg = pygame.image.load(name + str(0) + ".png")
            tmpImg = tmpImg.convert_alpha()
            width = width - 76 / Enemy.FADE_TIME
            height = height - 34 / Enemy.FADE_TIME
            tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
            self.mFramesFadeOut.append(tmpImg)
            i -= 1

        #Load the image sequence for the explosion
        self.mFramesExplosion = []
        self.setState(Enemy.START)
        i = 0
        while(i <= 9):
            num = "0" + str(i)
            tmpImg = pygame.image.load("assets/images/explosion" + num + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFramesExplosion.append(tmpImg)
            i += 1
        #self.mExplosionSound = pygame.mixer.Sound("assets/audio/enemy_explosion.wav")

    def hit(self):
        if (self.getState() == Enemy.START or self.getState() == Enemy.NORMAL or self.getState() == Enemy.EXITING):
            self.setState(Enemy.EXPLODING)
            GameData.inst().addScore1(self.mScore)

    def isStateNormal(self):
        return self.getState() == Enemy.NORMAL

    def initDroidOrbit(self):
        if(self.mOrbitCenter == []):
            x = random.randrange(self.mDistance, Game.inst().SCREEN_WIDTH-self.mDistance)
            y = random.randrange(self.mDistance, Game.inst().SCREEN_HEIGHT-self.mDistance)
            self.mOrbitCenter = [x, y]
            self.setX(x)
            self.setY(y)
        if ((self.getX() >= self.mOrbitCenter[0] + self.mDistance) or (self.getX() <= self.mOrbitCenter[0] - self.mDistance)):
            self.setX(self.getX() - self.getVelX())
            self.setVelX(-CMath.sign(self.getVelX()) * (random.randrange(-15, 15, 4)))
        elif ((self.getY() >= self.mOrbitCenter[1] + self.mDistance) or (self.getY() <= self.mOrbitCenter[1] - self.mDistance)):
            self.setY(self.getY() - self.getVelY())
            self.setVelY(-CMath.sign(self.getVelY()) * (random.randrange(-15, 15, 4)))



    def initSpeed(self):
        self.setVelX(random.randrange(-15, 15, 4))
        self.setVelY(random.randrange(-15, 15, 4))

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def setState(self, aState):
        AnimatedSprite.setState(self, aState)
        if (self.getState() == Enemy.START):
            self.initAnimation(self.mFramesFadeIn, 0, 0, False)
            self.mFadeTime = Enemy.FADE_TIME
        elif(self.getState() == Enemy.NORMAL):
            self.initAnimation(self.mFramesNormal, 0, 0, True)
        elif(self.getState() == Enemy.EXPLODING):
            self.initAnimation(self.mFramesExplosion, 0, 2, False)
            self.stopMove()
            #AudioManager.inst().play(self.mExplosionSound)
        elif (self.getState() == Enemy.EXITING):
            self.initAnimation(self.mFramesFadeOut, 0, 0, False)
            self.mFadeTime = Enemy.FADE_TIME

            
    
    def update(self):
        if (self.getState() == Enemy.START):
            self.mFadeTime -= 1
            if(self.mFadeTime <= 0):
                self.setState(Enemy.NORMAL)
                return
        elif (self.getState() == Enemy.NORMAL):
            self.mTimeAtSameSpeed += 1
            self.mTimeAlive += 1
            if(self.mTimeAlive > Enemy.LIFE_TIME):
                self.setState(Enemy.EXITING)
                return
            if (self.mTimeAtSameSpeed > self.mMaxTimeAtSameSpeed):
                self.initSpeed()
                self.mTimeAtSameSpeed = 0
                self.initDroidOrbit()
        elif (self.getState() == Enemy.EXPLODING):
            if ( self.isEnded() ):
                if(random.randint(0,100) % 6 == 0):
                    a = Pickup(Pickup.randomType())
                    a.setXY(self.getX(), self.getY())
                self.die()
                return
        elif (self.getState() == Enemy.EXITING):
            self.mFadeTime -= 1
            if (self.mFadeTime <= 0):
                GameData.inst().addInstability(1)
                self.die()
                return

        #Invoke update() from the super class for movement
        AnimatedSprite.update(self)


    
    def render(self,aScreen):
        AnimatedSprite.render(self, aScreen)


    #Destroys the object
    def destroy(self):
        AnimatedSprite.destroy(self)
        i = len(self.mFramesNormal)
        while i > 0:
            self.mFramesNormal[i-1] = None
            self.mFramesNormal.pop(i-1)
            i -= 1
        i = len(self.mFramesExplosion)
        while i > 0:
            self.mFramesExplosion[i-1] = None
            self.mFramesExplosion.pop(i-1)
            i -= 1

        i = len(self.mFramesFadeIn)
        while i > 0:
            self.mFramesFadeIn[i - 1] = None
            self.mFramesFadeIn.pop(i - 1)
            i -= 1
        i = len(self.mFramesFadeOut)
        while i > 0:
            self.mFramesFadeOut[i - 1] = None
            self.mFramesFadeOut.pop(i - 1)
            i -= 1
