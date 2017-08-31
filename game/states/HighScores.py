import pygame
from api.Keyboard import *
from api.Game import *
from api.GameState import *
from api.TextSprite import *


class HighScores(GameState):

    HIGH_SCORES = []

    def __init__(self):
        GameState.__init__(self)
        self.mImg = None
        self.mTextTitle = None
        self.mText = None
        self.mText2 = None
        self.mText3 = None
        self.mText4 = None
        self.mText5 = None
        self.mText6 = None
        self.mText7 = None
        self.mText8 = None
        self.mText9 = None
        self.mText10 = None
        self.mBack = None



    def init(self):
        GameState.init(self)
        self.mImg = pygame.image.load("assets/images/Background.png")
        self.mImg = self.mImg.convert()
        self.mImg = pygame.transform.scale(self.mImg, Game.RESOLUTION)
        Game.inst().setBackground(self.mImg)
        HighScores.getHighScores()
        self.mTextTitle = TextSprite("High Scores", 60, "assets/fonts/days.otf", Game.BLACK)
        self.mTextTitle.setXY((Game.SCREEN_WIDTH - self.mTextTitle.getWidth())/2, 30)
        self.mText = TextSprite("1) " + str(HighScores.HIGH_SCORES[0]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText.setXY(Game.SCREEN_WIDTH/4, 150)
        self.mText2 = TextSprite("2) " + str(HighScores.HIGH_SCORES[1]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText2.setXY(Game.SCREEN_WIDTH/4, 190)
        self.mText3 = TextSprite("3) " + str(HighScores.HIGH_SCORES[2]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText3.setXY(Game.SCREEN_WIDTH/4, 230)
        self.mText4 = TextSprite("4) " + str(HighScores.HIGH_SCORES[3]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText4.setXY(Game.SCREEN_WIDTH/4, 270)
        self.mText5 = TextSprite("5) " + str(HighScores.HIGH_SCORES[4]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText5.setXY(Game.SCREEN_WIDTH/4, 310)
        self.mText6 = TextSprite("6) " + str(HighScores.HIGH_SCORES[5]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText6.setXY(Game.SCREEN_WIDTH/4, 350)
        self.mText7 = TextSprite("7) " + str(HighScores.HIGH_SCORES[6]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText7.setXY(Game.SCREEN_WIDTH/4, 390)
        self.mText8 = TextSprite("8) " + str(HighScores.HIGH_SCORES[7]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText8.setXY(Game.SCREEN_WIDTH/4, 430)
        self.mText9 = TextSprite("9) " + str(HighScores.HIGH_SCORES[8]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText9.setXY(Game.SCREEN_WIDTH/4, 470)
        self.mText10 = TextSprite("10) " + str(HighScores.HIGH_SCORES[9]), 25, "assets/fonts/days.otf", Game.BLACK)
        self.mText10.setXY(Game.SCREEN_WIDTH/4, 510)
        self.mBack = TextSprite("[B] Back", 40, "assets/fonts/days.otf", Game.BLACK)
        self.mBack.setXY((Game.SCREEN_WIDTH - self.mBack.getWidth())/2, 620)

    @classmethod
    def addHighScore(cls,aScore):
        i = 0
        tmp = []
        included = False
        while(i < len(HighScores.HIGH_SCORES)):
            if(aScore >= int(HighScores.HIGH_SCORES[i]) and not included):
                tmp.append(aScore)
                tmp.append(int(HighScores.HIGH_SCORES[i]))
                included = True
            else:
                tmp.append(int(HighScores.HIGH_SCORES[i]))
            i += 1
        if(len(tmp) > len(HighScores.HIGH_SCORES)):
            tmp.pop()
        HighScores.HIGH_SCORES = tmp
        #problema es que highscore no updatea aunque temp si
        file = open("assets\data\HighScores.txt", "w")
        i = 0
        while (i < len(HighScores.HIGH_SCORES)):
            file.write(str(HighScores.HIGH_SCORES[i]))
            file.write("\n")
            i += 1
        file.close()


    @classmethod
    def getHighScores(cls):
        try:
            file = open("assets\data\HighScores.txt", "r")
            HighScores.HIGH_SCORES = []
            for line in file:
                HighScores.HIGH_SCORES.append(line)
            file.close()
            return HighScores.HIGH_SCORES
        except IOError:
            print("No HighScores.txt file in assets\data\ ")


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
        self.mText6.update()
        self.mText7.update()
        self.mText8.update()
        self.mText9.update()
        self.mText10.update()
        self.mBack.update()

    def render(self):
        GameState.render(self)
        self.mTextTitle.render(Game.inst().getScreen())
        self.mText.render(Game.inst().getScreen())
        self.mText2.render(Game.inst().getScreen())
        self.mText3.render(Game.inst().getScreen())
        self.mText4.render(Game.inst().getScreen())
        self.mText5.render(Game.inst().getScreen())
        self.mText6.render(Game.inst().getScreen())
        self.mText7.render(Game.inst().getScreen())
        self.mText8.render(Game.inst().getScreen())
        self.mText9.render(Game.inst().getScreen())
        self.mText10.render(Game.inst().getScreen())
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
        self.mText6.destroy()
        self.mText6 = None
        self.mText7.destroy()
        self.mText7 = None
        self.mText8.destroy()
        self.mText8 = None
        self.mText9.destroy()
        self.mText9 = None
        self.mText10.destroy()
        self.mText10 = None
        self.mBack.destroy()
        self.mBack = None


