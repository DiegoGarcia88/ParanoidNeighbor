import pygame
from api.AnimatedSprite import *
from api.Game import *
from game.EnemyManager import *
from api.Mouse import *

class MousePointer(AnimatedSprite):
    AIMED_TARGET = None
    def __init__(self):
        AnimatedSprite.__init__(self)
        self.mArray = []
        i = 0
        while (i < 2):
            img = pygame.image.load("assets/images/targetPointer0" + str(i) + ".png")
            img = img.convert_alpha()
            self.mArray.append(img)
            i += 1
        self.initAnimation(self.mArray,0,0,True)
        self.gotoAndStop(0)

    def update(self):
        AnimatedSprite.update(self)
        self.setXY(Mouse.inst().getX(), Mouse.inst().getY())
        self.overTarget()

    def overTarget(self):
        i = 0
        while (i < len(EnemyManager.inst().mArray)):
            enemy = EnemyManager.inst().mArray[i]
            if(self.collides(enemy)):
                self.gotoAndStop(1)
                MousePointer.AIMED_TARGET = enemy
                return
            else:
                self.gotoAndStop(0)
                MousePointer.AIMED_TARGET = None
            i += 1

    def render(self, aScreen):
        AnimatedSprite.render(self, aScreen)

    def destroy(self):
        AnimatedSprite.destroy(self)
