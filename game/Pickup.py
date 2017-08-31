import pygame
import random
import math
from api.CMath import *
from api.AnimatedSprite import *
from api.GameConstants import *
from game.EnemyManager import *
from api.AudioManager import *
from game.GameData import *


class Pickup(AnimatedSprite):
    #State machine
    START = 0
    NORMAL = 1
    EXPLODING = 2
    EXITING = 3
    FADE_TIME = 45
    LIFE_TIME = 90

    #Types

    INFINITE = 0
    HEAL = 1
    RELOAD = 2

    def __init__(self, aType):
        AnimatedSprite.__init__(self)
        self.mType = aType
        self.mFrames = []
        self.mTimeAlive = 0
        self.mScaleWidth = 0
        self.mScaleHeight = 0
        self.setScore(0)
        #Load Image sequence
        self.mFramesNormal = []
        self.mFadeTime = 0
        self.mFramesFadeIn = []
        self.mFramesFadeOut = []
        self.setRegistration(Sprite.CENTER)
        if(self.mType == Pickup.INFINITE):
            name = "assets/images/IBox0"
            i = 0
            while (i <= 3):
                tmpImg = pygame.image.load(name + str(i) + ".png")
                tmpImg = tmpImg.convert_alpha()
                # After changing from place holders to final art the drones(same size) look smaller so I am scaling them up 1.5x
                tmpImg = pygame.transform.scale(tmpImg, (150, 140))
                self.mFramesNormal.append(tmpImg)
                i += 1
            i = 0
            width = 0
            height = 0
            # TODO: change 75 and 70 from fixed values to original image width and height
            while (i < Pickup.FADE_TIME):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width + 75 / Pickup.FADE_TIME
                height = height + 70 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeIn.append(tmpImg)
                i += 1
            i = Pickup.FADE_TIME
            width = 150
            height = 140
            while (i > 0):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width - 150 / Pickup.FADE_TIME
                height = height - 140 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeOut.append(tmpImg)
                i -= 1

        if (self.mType == Pickup.HEAL):
            name = "assets/images/HBox0"
            i = 0
            while (i <= 3):
                tmpImg = pygame.image.load(name + str(i) + ".png")
                tmpImg = tmpImg.convert_alpha()
                # After changing from place holders to final art the drones(same size) look smaller so I am scaling them up 1.5x
                tmpImg = pygame.transform.scale(tmpImg, (150, 140))
                self.mFramesNormal.append(tmpImg)
                i += 1
            i = 0
            width = 0
            height = 0
            # TODO: change 75 and 70 from fixed values to original image width and height
            while (i < Pickup.FADE_TIME):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width + 75 / Pickup.FADE_TIME
                height = height + 70 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeIn.append(tmpImg)
                i += 1
            i = Pickup.FADE_TIME
            width = 150
            height = 140
            while (i > 0):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width - 150 / Pickup.FADE_TIME
                height = height - 140 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeOut.append(tmpImg)
                i -= 1

        if (self.mType == Pickup.RELOAD):
            name = "assets/images/RBox0"
            i = 0
            while (i <= 3):
                tmpImg = pygame.image.load(name + str(i) + ".png")
                tmpImg = tmpImg.convert_alpha()
                # After changing from place holders to final art the drones(same size) look smaller so I am scaling them up 1.5x
                tmpImg = pygame.transform.scale(tmpImg, (150, 140))
                self.mFramesNormal.append(tmpImg)
                i += 1
            i = 0
            width = 0
            height = 0
            # TODO: change 75 and 70 from fixed values to original image width and height
            while (i < Pickup.FADE_TIME):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width + 75 / Pickup.FADE_TIME
                height = height + 70 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeIn.append(tmpImg)
                i += 1
            i = Pickup.FADE_TIME
            width = 150
            height = 140
            while (i > 0):
                tmpImg = pygame.image.load(name + str(0) + ".png")
                tmpImg = tmpImg.convert_alpha()
                width = width - 150 / Pickup.FADE_TIME
                height = height - 140 / Pickup.FADE_TIME
                tmpImg = pygame.transform.scale(tmpImg, (int(math.ceil(width)), int(math.ceil(height))))
                self.mFramesFadeOut.append(tmpImg)
                i -= 1

        #Load the image sequence for the explosion
        self.mFramesExplosion = []
        self.setState(Pickup.START)
        i = 0
        while(i <= 9):
            num = "0" + str(i)
            tmpImg = pygame.image.load("assets/images/explosion" + num + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFramesExplosion.append(tmpImg)
            i += 1
        #self.mExplosionSound = pygame.mixer.Sound("assets/audio/enemy_explosion.wav")
        EnemyManager.inst().add(self)


    def getType(self):
        return self.mType

    def hit(self):
        if (self.getState() == Pickup.START or self.getState() == Pickup.NORMAL or self.getState() == Pickup.EXITING):
            self.setState(Pickup.EXPLODING)
            GameData.inst().addScore1(self.mScore)

    def isStateNormal(self):
        return self.getState() == Pickup.NORMAL

    @classmethod
    def randomType(cls):
        return random.choice([Pickup.HEAL, Pickup.INFINITE, Pickup.RELOAD])

    def initSpeed(self):
        self.setVelX(random.randrange(-15, 15, 4))
        self.setVelY(random.randrange(-15, 15, 4))

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def setState(self, aState):
        AnimatedSprite.setState(self, aState)
        if (self.getState() == Pickup.START):
            self.initAnimation(self.mFramesFadeIn, 0, 0, False)
            self.mFadeTime = Pickup.FADE_TIME
        elif(self.getState() == Pickup.NORMAL):
            self.initAnimation(self.mFramesNormal, 0, 0, True)
        elif(self.getState() == Pickup.EXPLODING):
            self.initAnimation(self.mFramesExplosion, 0, 2, False)
            #AudioManager.inst().play(self.mPickupSound)
            from api.Game import Game
            if(self.getType() == Pickup.RELOAD):
                if(Game.inst().getState().mPlayer.TIME_RELOADING) > 30:
                    Game.inst().getState().mPlayer.TIME_RELOADING = Game.inst().getState().mPlayer.TIME_RELOADING - 10
                    print(Game.inst().getState().mPlayer.TIME_RELOADING)
            if (self.getType() == Pickup.INFINITE and Game.inst().getState().mPlayer.getEffect() == False):
                Game.inst().getState().mPlayer.setEffect(True)
                Game.inst().getState().mPlayer.setEffectTime(300)
                Game.inst().getState().mPlayer.setBullets(999)
            if (self.getType() == Pickup.HEAL and GameData.inst().getInstability() > 0):
                GameData.inst().addInstability(-1)
        elif (self.getState() == Pickup.EXITING):
            self.initAnimation(self.mFramesFadeOut, 0, 0, False)
            self.mFadeTime = Pickup.FADE_TIME



    def update(self):
        if (self.getState() == Pickup.START):
            self.mFadeTime -= 1
            if(self.mFadeTime <= 0):
                self.setState(Pickup.NORMAL)
                return
        elif (self.getState() == Pickup.NORMAL):
            self.mTimeAlive += 1
            if(self.mTimeAlive > Pickup.LIFE_TIME):
                self.setState(Pickup.EXITING)
                return
        elif (self.getState() == Pickup.EXPLODING):
            if ( self.isEnded() ):
                self.die()
                return
        elif (self.getState() == Pickup.EXITING):
            self.mFadeTime -= 1
            if (self.mFadeTime <= 0):
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
