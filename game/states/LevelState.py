import pygame
import random
from api.GameState import *
from api.Game import *
from game.Enemy import *
from game.Player import *
from game.GameData import *
from api.GameConstants import *
from api.TextSprite import *
from game.FillerBar import *
from game.states.HighScores import *
from game.DisplayBullets import *
from game.Clouds import *
from api.AudioManager import *


class LevelState(GameState):
    #LEVEL STATE MACHINE
    PLAYING = 0
    INIT_LEVEL = 1
    TRANSITION = 2
    GAME_OVER = 3
    
    TIME_SHOWING_LEVEL_TEXT = Game.FPS * 2
    TIME_TRANSITION = Game.FPS * 1
    TIME_SHOWING_GAME_OVER = Game.FPS * 4
    SPAWN_TIME = 90
    MAX_ENEMIES = 10
    ENEMIES_PER_INIT = 1
        
    def __init__(self):
        GameState.__init__(self)
        self.mImg = None
        self.mEnemyCounter = 0
        self.mPlayer = Player()
        self.mTimeState = 0
        self.mSpawnTimeCounter = 0
        self.mPlayer.setXY(20, Game.SCREEN_HEIGHT - self.mPlayer.getHeight() - 20)
        self.mPlayer.setBounds(0, Game.SCREEN_WIDTH - self.mPlayer.getWidth(), -self.mPlayer.getHeight(), Game.SCREEN_HEIGHT)
        self.mPlayer.setBoundAction(GameObject.STOP)
        self.mPlayerScore = TextSprite("SCORE: " + str(GameData.inst().getScore1()), 40, "assets/fonts/days.otf", Game.WHITE)
        self.mPlayerScore.setXY((Game.SCREEN_WIDTH-self.mPlayerScore.getWidth())/2, Game.SCREEN_HEIGHT-self.mPlayerScore.getHeight()*2)
        self.mBulletDisplay = DisplayBullets()
        self.mBulletDisplay.setXY(self.mBulletDisplay.getWidth(), self.mBulletDisplay.getHeight()/2)
        #Cambiar instability display por la barra eventualmente
        self.mFullInstability = FillerBar("assets/images/fullBar.png")
        self.mInnerFilling = FillerBar("assets/images/fullBar.png")
        #el 10 sale de la diferencia entre frame bar y full instability, dividido 2
        self.mFullInstability.setXY((Game.SCREEN_WIDTH - self.mFullInstability.getWidth()) / 2, 10)
        self.mEmptyInstability = FillerBar("assets/images/emptyBar.png")
        self.mEmptyInstability.setXY((Game.SCREEN_WIDTH - self.mEmptyInstability.getWidth()) / 2, 10)
        self.mBarFrame = Sprite()
        img = pygame.image.load("assets/images/barFrame.png")
        img = img.convert_alpha()
        self.mBarFrame.setImage(img)
        self.mBarFrame.setXY((Game.SCREEN_WIDTH - self.mBarFrame.getWidth()) / 2, 0)
        self.mReloadingText = TextSprite("Reloading...", 60, "assets/fonts/days.otf", Game.BLACK)
        self.mReloadingText.setXY((Game.SCREEN_WIDTH - self.mReloadingText.getWidth()) / 2, (Game.SCREEN_HEIGHT - self.mReloadingText.getHeight())/2)
        self.mImg = pygame.image.load("assets/images/Background00.png")
        self.mImg = self.mImg.convert()
        self.mImg = pygame.transform.scale(self.mImg, Game.RESOLUTION)
        self.mBackgroundTop = pygame.image.load("assets/images/Background01.png")
        self.mBackgroundTop = self.mBackgroundTop.convert_alpha()
        self.mBackgroundTop = pygame.transform.scale(self.mBackgroundTop, Game.RESOLUTION)
        Game.inst().setBackground(self.mImg)
        GameData.inst().setScore1(0)
        AudioManager.inst().loadSongs(["assets/audio/Justin Mahar - The Grind.ogg", "assets/audio/Purple Planet Music - Palpitations.ogg"])
        AudioManager.inst().setSongEnd()
        AudioManager.inst().playRandom()
        self.mLevel = 1
        self.mText = None
        self.mState = 0
        self.setState(LevelState.INIT_LEVEL)
        self.initEnemies(LevelState.ENEMIES_PER_INIT)
        self.mClouds = Clouds(-2, 2)
        GameData.inst().setInstability(0)
        HighScores.getHighScores()



    def reinit(self):
        self.mTimeState = 0
        self.mSpawnTimeCounter = 0

    def setState(self, aState):
        self.mState = aState
        self.mTimeState = 0
        if (self.mState == LevelState.INIT_LEVEL):
            self.mText = TextSprite("Level " + str(self.mLevel), 60, "assets/fonts/days.otf", Game.WHITE)
            self.mText.setXY((Game.SCREEN_WIDTH - self.mText.getWidth())/2, 300)
            return
        elif(self.mState == LevelState.TRANSITION):
            return
        elif(self.mState == LevelState.PLAYING):
            return
        elif(self.mState == LevelState.GAME_OVER):
            self.mText = TextSprite("GAME OVER", 80, "assets/fonts/days.otf", Game.WHITE)
            self.mText.setXY((Game.SCREEN_WIDTH - self.mText.getWidth())/2, 250)
            HighScores.addHighScore(GameData.inst().getScore1())
            return

    def adjustInstabilityBar(self,aBar):
        cur = GameData.inst().getInstability()
        maximum = GameData.inst().INSTABILITY_THRESHOLD
        coeficient = cur/maximum
        bar = pygame.transform.scale(aBar.getImage(), (int(coeficient * aBar.getWidth()), aBar.getHeight()))
        return bar

    def update(self):
        GameState.update(self)
        self.mClouds.update()
        self.mTimeState += 1
        self.mPlayerScore.update()
        self.mEmptyInstability.update()
        self.mFullInstability.setImage(self.adjustInstabilityBar(self.mInnerFilling))
        self.mFullInstability.update()
        self.mReloadingText.update()
        self.mBulletDisplay.update()
        self.mBulletDisplay.setBullets(self.mPlayer.mBullets)
        if(self.mState == LevelState.INIT_LEVEL):
            if(self.mTimeState > LevelState.TIME_SHOWING_LEVEL_TEXT):
                self.setState(LevelState.PLAYING)
                return
            self.mText.update()
        elif(self.mState == LevelState.PLAYING):
            self.mPlayer.update()
            self.mSpawnTimeCounter += 1
            if(GameData.inst().getInstability() == GameData.INSTABILITY_THRESHOLD):
                self.mPlayer.setState(Player.GAME_OVER)
            if (self.mPlayer.isGameOver()):
                self.setState(LevelState.GAME_OVER)
                return
            if (self.mEnemyCounter == LevelState.MAX_ENEMIES and GameData.inst().getInstability() < GameData.INSTABILITY_THRESHOLD and len(EnemyManager.inst().mArray) == 0):##WINNING CONDITION
                self.setState(LevelState.TRANSITION)
                return
        elif(self.mState == LevelState.TRANSITION):
            if(self.mTimeState > LevelState.TIME_TRANSITION):
                if(LevelState.SPAWN_TIME >= 60):
                    LevelState.SPAWN_TIME -= 10
                if(self.mLevel%3 == 0):
                    LevelState.MAX_ENEMIES += 1
                self.mEnemyCounter = 0
                self.nextLevel()
                return
        elif(self.mState == LevelState.GAME_OVER):
            if (self.mTimeState > LevelState.TIME_SHOWING_GAME_OVER):
                pygame.mixer.music.stop()
                from game.states.MenuState import MenuState
                nextState = MenuState()
                Game.inst().setState(nextState)
            self.mText.update()

        EnemyManager.inst().update()
        if(self.mSpawnTimeCounter == LevelState.SPAWN_TIME and self.mEnemyCounter < LevelState.MAX_ENEMIES):
            self.initEnemies(LevelState.ENEMIES_PER_INIT)
            self.mSpawnTimeCounter = 0


    def render(self):
        GameState.render(self)
        screen = Game.inst().getScreen()
        self.mClouds.render(screen)
        Game.inst().getScreen().blit(self.mBackgroundTop, (0, 0))
        self.mEmptyInstability.render(screen)
        self.mFullInstability.render(screen)
        self.mBarFrame.render(screen)
        EnemyManager.inst().render(screen)
        self.mPlayer.render(screen)
        self.mPlayerScore.setText("SCORE: " + str(GameData.inst().getScore1()))
        self.mPlayerScore.render(screen)
        self.mBulletDisplay.render(screen)
        if(self.mPlayer.getState() == Player.RELOADING):
            self.mReloadingText.render(screen)
        if (self.mState == LevelState.INIT_LEVEL or self.mState == LevelState.GAME_OVER):
            self.mText.render(screen)

    def nextLevel(self):
        self.mLevel += 1
        self.setState(LevelState.INIT_LEVEL)
        self.reinit()


    def initEnemies(self,aAmount):
        c = 0
        while (c < aAmount):
            n = Enemy()
            n.initDroidOrbit()
            n.initSpeed()
            #TODO: 180 and 90 hardcoded, need to find the right proportion of screenwidth
            n.setBounds(180, Game.SCREEN_WIDTH - n.getWidth() - 180, 90, Game.SCREEN_HEIGHT - n.getHeight() - 90)
            n.setBoundAction(GameObject.BOUNCE)
            EnemyManager.inst().addEnemy(n)
            self.mEnemyCounter += 1
            c += 1

    def destroy(self):
        GameState.destroy(self)
        self.mPlayer.destroy()
        self.mPlayer = None
        self.mPlayerScore.destroy()
        self.mEmptyInstability.destroy()
        self.mClouds.destroy()
        EnemyManager.inst().destroy()
        GameData.inst().destroy()







