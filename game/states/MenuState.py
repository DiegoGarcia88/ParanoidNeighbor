import pygame
from api.Keyboard import *
from api.Game import *
from api.GameState import *
from api.TextSprite import *


class MenuState(GameState):
    
    def __init__(self):
        GameState.__init__(self)
        self.mImg = None
        self.mTextTitle = None
        self.mTextInstructions = None


    def init(self):
        GameState.init(self)
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("assets/audio/Justin Mahar - Pumped.ogg")
            pygame.mixer.music.play(-1)
        self.mImg = pygame.image.load("assets/images/Background.png")
        self.mImg = self.mImg.convert()
        self.mImg = pygame.transform.scale(self.mImg, Game.RESOLUTION)
        Game.inst().setBackground(self.mImg)
        self.mTextTitle = TextSprite("Paranoid Neighbor", 60, "assets/fonts/days.otf", Game.WHITE)
        self.mTextTitle.setXY((Game.SCREEN_WIDTH - self.mTextTitle.getWidth())/2, 50)
        self.mTextInstructions = TextSprite("[S] Start, [C] Credits, [I] Instructions, [H] High Scores", 40, "assets/fonts/days.otf", Game.WHITE)
        self.mTextInstructions.setXY((Game.SCREEN_WIDTH - self.mTextInstructions.getWidth())/2, 600)

    def update(self):
        GameState.update(self)
        if Keyboard.inst().sKey():
            from game.states.LevelState import LevelState
            nextState = LevelState()
            Game.inst().setState(nextState)
            return
        if Keyboard.inst().cKey():
            from game.states.CreditsState import CreditsState
            nextState = CreditsState()
            Game.inst().setState(nextState)
            return
        if Keyboard.inst().iKey():
            from game.states.InstructionState import InstructionState
            nextState = InstructionState()
            Game.inst().setState(nextState)
            return
        if Keyboard.inst().hKey():
            from game.states.HighScores import HighScores
            nextState = HighScores()
            Game.inst().setState(nextState)
            return
        self.mTextTitle.update()
        self.mTextInstructions.update()

    def render(self):
        GameState.render(self)
        self.mTextTitle.render(Game.inst().getScreen())
        self.mTextInstructions.render(Game.inst().getScreen())

    def destroy(self):
        GameState.destroy(self)
        self.mImg = None
        self.mTextTitle.destroy()
        self.mTextTitle = None
        self.mTextInstructions.destroy()
        self.mTextInstructions = None


