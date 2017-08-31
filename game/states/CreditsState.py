import pygame
from api.Keyboard import *
from api.Game import *
from api.GameState import *
from api.TextSprite import *


class CreditsState(GameState):
    
    def __init__(self):
        GameState.__init__(self)
        self.mImg = None
        self.mTextTitle = None
        self.mTextContent = None
        self.mTextContactInfo = None
        self.mBack = None


    def init(self):
        GameState.init(self)
        self.mImg = pygame.image.load("assets/images/Background.png")
        self.mImg = self.mImg.convert()
        self.mImg = pygame.transform.scale(self.mImg, Game.RESOLUTION)
        Game.inst().setBackground(self.mImg)
        self.mTextTitle = TextSprite("Credits", 60, "assets/fonts/days.otf", Game.BLACK)
        self.mTextTitle.setXY((Game.SCREEN_WIDTH - self.mTextTitle.getWidth())/2, 30)
        self.mTextContent = TextSprite("Game Design, Programming and Art: Diego Garcia", 25, "assets/fonts/days.otf", Game.BLACK)
        self.mTextContent.setXY((Game.SCREEN_WIDTH - self.mTextContent.getWidth())/2, 120)
        self.mTextContactInfo = TextSprite("Email: diegogarcia19188@gmail.com", 20, "assets/fonts/days.otf", Game.BLACK)
        self.mTextContactInfo.setXY((Game.SCREEN_WIDTH - self.mTextContactInfo.getWidth())/2, 450)
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
        self.mTextContent.update()
        self.mTextContactInfo.update()
        self.mBack.update()

    def render(self):
        GameState.render(self)
        self.mTextTitle.render(Game.inst().getScreen())
        self.mTextContent.render(Game.inst().getScreen())
        self.mTextContactInfo.render(Game.inst().getScreen())
        self.mBack.render(Game.inst().getScreen())

    def destroy(self):
        GameState.destroy(self)
        self.mImg = None
        self.mTextTitle.destroy()
        self.mTextTitle = None
        self.mTextContent.destroy()
        self.mTextContent = None
        self.mTextContactInfo.destroy()
        self.mTextContactInfo = None
        self.mBack.destroy()
        self.mBack = None


