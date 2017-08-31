import pygame

from api.AnimatedSprite import *
from api.Keyboard import *
from api.GameConstants import *
from game.EnemyManager import *
from api.AudioManager import *
from game.GameData import *
from game.MousePointer import *

class Player(AnimatedSprite):
    #State machine
    NORMAL = 1
    DYING = 2
    GAME_OVER = 3
    RELOADING = 4
    #TIME DEATH LASTS (in FRAMES)
    TIME_DYING = 30
    TIME_RELOADING = 60
    MAX_BULLETS = 2
    TIME_BETWEEN_SHOTS = 15
    #Constructor
    #Parameters
    #aImgFile: image name to load
    def __init__(self):
        AnimatedSprite.__init__(self)
        self.setState(Player.NORMAL)
        self.mReloadCount = 0
        self.mTimeBetweenShots = 0
        self.mShootSound = pygame.mixer.Sound("assets/audio/shotgun_blast_v2.wav")
        self.mSoundCannotShoot = pygame.mixer.Sound("assets/audio/player_cannot_shoot.wav")
        self.mReloadSound = pygame.mixer.Sound("assets/audio/reload_shotgun.wav")
        self.mBullets = 2
        self.mEffectTime = 0
        self.mEffectActive = False

    def setEffectTime(self,aTime):
        self.mEffectTime = aTime

    def setEffect(self, aEffect):
        self.mEffectActive = aEffect

    def getEffect(self):
        return self.mEffectActive

    def getBullets(self):
        return self.mBullets

    def setBullets(self,aBullets):
        self.mBullets = aBullets

    def move(self):
        if(Mouse.inst().fire()):
            self.shoot()
        ##Reload the shotgun if not full and not reloading
        if (Keyboard.inst().rKey() and self.mBullets < Player.MAX_BULLETS and  self.getState() != Player.RELOADING):
            self.setState(Player.RELOADING)

    def shoot(self):
        if(self.canShoot()):
            AudioManager.inst().play(self.mShootSound)
            if(MousePointer.AIMED_TARGET != None):
                enemy = MousePointer.AIMED_TARGET
                enemy.hit()
            self.mBullets = self.mBullets - 1
            self.mTimeBetweenShots = Player.TIME_BETWEEN_SHOTS
        else:
            AudioManager.inst().play(self.mSoundCannotShoot)

    def canShoot(self):
        if(self.mBullets > 0 and self.mTimeBetweenShots <= 0):
            return True
        else:
            return False


    def update(self):
        if (self.mTimeBetweenShots > 0):
            self.mTimeBetweenShots = self.mTimeBetweenShots - 1
        if(self.mEffectTime > 0):
            self.mEffectTime -= 1
            if (self.mEffectTime == 0):
                self.setBullets(2)
                self.mEffectActive = False
        if (self.getState() == Player.NORMAL):
            if (GameData.mInstability > GameData.inst().INSTABILITY_THRESHOLD):
                self.setState(Player.DYING)
                return
            self.move()
        elif(self.getState() == Player.RELOADING):
            self.mReloadCount -= 1
            if (self.mReloadCount == 0):
                self.mBullets = Player.MAX_BULLETS
                self.setState(Player.NORMAL)
                return
        elif (self.getState() == Player.DYING):
            if (self.getTimeState() > Player.TIME_DYING):
                self.setState(Player.GAME_OVER)
                return
        elif (self.getState() == Player.GAME_OVER):
            return



    def setState(self,aState):
        AnimatedSprite.setState(self, aState)
        if(self.getState() == Player.DYING):
            pass
        elif(self.getState() == Player.NORMAL):
            pass
        elif self.getState() == Player.GAME_OVER:
            pass
        elif(self.getState() == Player.RELOADING):
            self.mReloadCount = Player.TIME_RELOADING
            AudioManager.inst().play(self.mReloadSound, 1)


    def isGameOver(self):
        return self.getState() == Player.GAME_OVER

    #Destroys the object
    def destroy(self):
        pass

