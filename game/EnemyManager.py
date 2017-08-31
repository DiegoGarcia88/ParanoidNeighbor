import pygame
from api.Manager import *
from api.Game import *

class EnemyManager(Manager):
    mInstance = None
    mInitialized = False

    def __new__(self, *args, **kargs):
        if(EnemyManager.mInstance is None):
            EnemyManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(EnemyManager.mInstance)
        else:
            print("Careful, EnemyManager() shouldn't be instanced more than once, use EnemyManager.inst()")
        return self.mInstance

    @classmethod

    def inst(cls):
        if(not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (EnemyManager.mInitialized):
            return
        EnemyManager.mInitialized = True
        Manager.__init__(self)


    def setVelX(self,aMinVelX):
        self.mVelX = aMinVelX
        i = 0
        while(i < len(self.mArray)):
            self.mArray[i].setVelX(self.mVelX)
            i += 1

    def update(self):
        Manager.update(self)

    def render(self, aScreen):
        Manager.render(self,aScreen)

    def addEnemy(self,aEnemy):
        Manager.add(self, aEnemy)

    def destroy(self):
        Manager.destroy(self)
        EnemyManager.mInstance = None
