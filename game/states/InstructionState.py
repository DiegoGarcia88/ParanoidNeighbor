import pygame
from api.Keyboard import *
from api.Game import *
from api.GameState import *
from api.TextSprite import *


class InstructionState(GameState):

    def __init__(self):
        GameState.__init__(self)
        self.mImg = None
        self.mTextTitle = None
        self.mText = None
        self.mText2 = None
        self.mText3 = None
        self.mText4 = None
        self.mText5 = None
        self.mBack = None


    def init(self):
        GameState.init(self)
        self.mImg = pygame.image.load("assets/images/Background.png")
        self.mImg = self.mImg.convert()
        self.mImg = pygame.transform.scale(self.mImg, Game.RESOLUTION)
        Game.inst().setBackground(self.mImg)
        self.mTextTitle = TextSprite("Instructions", 60, "assets/fonts/days.otf", Game.BLACK)
        self.mTextTitle.setXY((Game.SCREEN_WIDTH - self.mTextTitle.getWidth())/2, 30)
        self.mText = TextSprite("[Left Click] Shoot", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText.setXY((Game.SCREEN_WIDTH - self.mText.getWidth())/2, 150)
        self.mText2 = TextSprite("[P] Pause", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText2.setXY((Game.SCREEN_WIDTH - self.mText2.getWidth())/2, 250)
        self.mText3 = TextSprite("[F] FullScreen", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText3.setXY((Game.SCREEN_WIDTH - self.mText3.getWidth())/2, 350)
        self.mText4 = TextSprite("[R] Reload", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText4.setXY((Game.SCREEN_WIDTH - self.mText4.getWidth())/2, 450)
        self.mText5 = TextSprite("[ESC] Exit Game", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText5.setXY((Game.SCREEN_WIDTH - self.mText5.getWidth())/2, 550)
        self.mBack = TextSprite("[B] Back", 40, "assets/fonts/days.otf", Game.BLACK)
        self.mBack.setXY((Game.SCREEN_WIDTH - self.mBack.getWidth())/2, 620)


    def update(self):
        GameState.update(self)
        if Keyboard.inst().bKey():
            from game.states.MenuState import MenuState
            nextState = MenuState()
            Game.inst().setState(nextState)
            return
        self.mTextTitle.update()
        self.mText.update()
        self.mText2.update()
        self.mText3.update()
        self.mText4.update()
        self.mText5.update()
        self.mBack.update()

    def render(self):
        GameState.render(self)
        self.mTextTitle.render(Game.inst().getScreen())
        self.mText.render(Game.inst().getScreen())
        self.mText2.render(Game.inst().getScreen())
        self.mText3.render(Game.inst().getScreen())
        self.mText4.render(Game.inst().getScreen())
        self.mText5.render(Game.inst().getScreen())
        self.mBack.render(Game.inst().getScreen())

    def destroy(self):
        GameState.destroy(self)
        self.mImg = None
        self.mTextTitle.destroy()
        self.mTextTitle = None
        self.mText.destroy()
        self.mText = None
        self.mText2.destroy()
        self.mText2 = None
        self.mText3.destroy()
        self.mText3 = None
        self.mText4.destroy()
        self.mText4 = None
        self.mText5.destroy()
        self.mText5 = None
        self.mBack.destroy()
        self.mBack = None


