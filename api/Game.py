import pygame

from api.Keyboard import *
from api.GameConstants import *
from api.Mouse import *
from api.AudioManager import *
from api.TextSprite import *
import gc

class Game(object):
    mInstance = None
    mInitialized = False
    mScreen = None
    mBackground = None
    mClock = None
    mQuit = False
    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0
    RESOLUTION = 0
    mIsFullScreen = True
    mIsPaused = False
    mTextPause = None
    mShowGamePointer = False
    #Create color constants
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    CYAN = (0, 255, 255)
    PINK = (255, 0, 255)
    YELLOW = (255, 255, 0)
    FPS = 30
    STARTING_SHIPS = 0

    def __new__(self,*args,**kargs):
        if (Game.mInstance is None):
            Game.mInstance = object.__new__(self,*args,**kargs)
            self.init(Game.mInstance)
        else:
            print("Careful: Game(): Shouldn't be instanced more than once. Use Game.inst()")
        return self.mInstance
    
    @classmethod
    def inst(cls):
        if(not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        Game.SCREEN_WIDTH = GameConstants.inst().SCREEN_WIDTH
        Game.SCREEN_HEIGHT = GameConstants.inst().SCREEN_HEIGHT
        Game.RESOLUTION = (Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)
        pygame.mixer.init(44100, -16, 8, 512)
        pygame.init()
        Game.mScreen = pygame.display.set_mode(Game.RESOLUTION,pygame.FULLSCREEN)
        pygame.display.set_caption("Paranoid Neighbor")
        Game.mBackground = pygame.Surface(Game.mScreen.get_size())
        Game.mBackground = self.mBackground.convert()
        Game.mClock = pygame.time.Clock()
        Game.mQuit = False
        pygame.mouse.set_visible(False)
        Game.mMousePointer = MousePointer()
        Game.mState = None
        Game.mIsPaused = False
        self.showGamePointer(True)
        Game.mTextPause = TextSprite("Pause [P] or [Enter]", 60, "assets/fonts/days.otf", Game.WHITE)
        Game.mTextPause.setXY((Game.SCREEN_WIDTH - Game.mTextPause.getWidth())/2, (Game.SCREEN_HEIGHT - Game.mTextPause.getHeight())/2)
        Game.STARTING_SHIPS = 2


    #Tells the system if we use a game pointer or the default
    def showGamePointer(self, aShowGamePointer):
        Game.mShowGamePointer = aShowGamePointer
        if (aShowGamePointer):
            pygame.mouse.set_visible(False)
            Game.mMousePointer = MousePointer()
        else:
            pygame.mouse.set_visible(True)
            if(Game.mMousePointer != None):
                Game.mMousePointer.destroy()
                Game.mMousePointer = None
    def setState(self, aState):
        if(Game.mState != None):
            Game.mState.destroy()
            Game.mState = None
            print(gc.collect(), "deleted objects")
        Game.mState = aState
        Game.mState.init()

    def gameLoop(self):
        while (not self.mQuit):
            Game.mClock.tick(30)
            Keyboard.inst().update()
            Mouse.inst().update()
            if(Game.mMousePointer != None):
                Game.mMousePointer.update()
            for event in pygame.event.get():
                #if window is closed, exit game
                if (event.type == pygame.QUIT):
                    Game.mQuit = True
                #If [ESC] is pressed, quit game
                if(event.type==pygame.KEYDOWN):
                    Keyboard.inst().keyDown(event.key)
                    if(event.key==pygame.K_ESCAPE):
                        Game.mQuit = True
                    #if F is pressed go full screen
                    if(event.key==pygame.K_f):
                        Game.mIsFullScreen = not Game.mIsFullScreen
                        if(Game.mIsFullScreen):
                            Game.mScreen = pygame.display.set_mode(Game.RESOLUTION,pygame.FULLSCREEN)
                        else:
                            Game.mScreen = pygame.display.set_mode(Game.RESOLUTION)
                elif(event.type==pygame.KEYUP):
                    Keyboard.inst().keyUp(event.key)
                if (event.type == AudioManager.inst().SONG_END):
                    print("randomizing")
                    AudioManager.inst().playRandom()

            if (Keyboard.inst().pauseKey()):
                              self.togglePause()
            Game.mScreen.blit(self.mBackground, (0, 0))
            Game.mTextPause.update()
            if (not Game.mIsPaused):
                              #Update Function
                              Game.mState.update()
            #Render Function
            Game.mState.render()

            if (Game.mIsPaused):
                Game.mTextPause.render(self.mScreen)

            if(Game.mMousePointer != None):
                Game.mMousePointer.render(self.mScreen)

            pygame.display.flip()

    def setBackground(self, aBackgroundImage):
        Game.mBackground = None
        Game.mBackground = aBackgroundImage
        self.blitBackground(Game.mBackground)

    def blitBackground(self,aBackground):
        Game.mScreen.blit(aBackground, (0, 0))

    def togglePause(self):
        Game.mIsPaused = not Game.mIsPaused
                              
    def getScreen(self):
        return Game.mScreen

    def getState(self):
        return self.mState

    def destroy(self):
        if(Game.mState != None):
            Game.mState.destroy()
            Game.mState = None
        Keyboard.inst().destroy()
        Mouse.inst().destroy()
        if(Game.mMousePointer != None):
            Game.mMousePointer.destroy()
            Game.mMousePointer = None
        Game.mTextPause.destroy()
        Game.mTextPause = None
        pygame.mouse.set_visible(True)
        Game.mInstance = None
        pygame.quit()        
from game.MousePointer import *