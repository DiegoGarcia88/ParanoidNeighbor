import pygame

class GameData(object):
    mInstance = None
    mInitialized = False
    mScore1 = 0
    mInstability = 0
    INSTABILITY_THRESHOLD = 10

    def __new__(self, *args, **kargs):
        if (GameData.mInstance is None):
            GameData.mInstance = object.__new__(self, *args, **kargs)
            self.init(GameData.mInstance)
        else:
            print ("Careful: GameData(): shouldn't be instanced more than once. Use GameData.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (GameData.mInitialized):
            return
        GameData.mInitialized = True
        GameData.mScore1 = 0
        GameData.mLives1 = 0
        

    def setScore1(self, aScore):
        GameData.mScore1 = aScore
        self.controlScores()

    def addScore1(self, aScore):
        GameData.mScore1 += aScore
        self.controlScores()

   
    def controlScores(self):
    #Check for negative scores and too large scores and cap them
        if (GameData.mScore1 < 0):
            GameData.mScore1 = 0
        if (GameData.mScore1 > 999999):
            GameData.mScore1 = 999999
        
    def getScore1(self):
        return GameData.mScore1

    def setInstability(self, aInstability):
        GameData.mInstability = aInstability
        self.controlInstability()

    def addInstability(self, aInstability):
        GameData.mInstability += aInstability
        self.controlInstability()

    def controlInstability(self):
    #Check for negative and too large paranoia and cap them
        if (GameData.mInstability < 0):
            GameData.mInstability = 0
        if (GameData.mInstability > GameData.INSTABILITY_THRESHOLD):
            GameData.mInstability = GameData.INSTABILITY_THRESHOLD
        
    def getInstability(self):
        return GameData.mInstability

    def destroy(self):
        GameData.mInstance = None
