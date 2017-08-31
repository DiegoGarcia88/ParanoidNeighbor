class GameObject(object):
    #Border Behaviours
    NONE = 0
    STOP = 1
    WRAP = 2
    BOUNCE = 3
    DIE = 4
    
    #Color of ships
    COLOR_BLUE = 0
    COLOR_RED = 1
    COLOR_GREEN = 2
    COLOR_YELLOW = 3
    #Type of GameObjects
    TYPE_ENEMY = 0
    TYPE_PLAYER = 1
    TYPE_PROYECTILE = 2
    def __init__(self):
        self.mX = 0
        self.mY = 0
        self.mMinX = 0
        self.mMaxX = 0
        self.mMinY = 0
        self.mMaxY = 0
        self.mVelX = 0
        self.mVelY = 0
        self.mAccelX = 0
        self.mAccelY = 0
        self.mBoundAction = GameObject.NONE
        self.mIsDead = False
        self.mState = 0
        self.mTimeState = 0
    #Defines border behaviour
    def setBoundAction(self, aBoundAction):
        self.mBoundAction = aBoundAction

    def checkBounds(self):
        #If none, we don't check border collision
        if (self.mBoundAction == GameObject.NONE):
            return
        #Which borders we are touching
        left = (self.mX < self.mMinX)
        right = (self.mX > self.mMaxX)
        up = (self.mY < self.mMinY)
        down = (self.mY > self.mMaxY)
        
        #If no collisions, we don't do anything
        if not (left or right or up or down):
            return
        if (self.mBoundAction == GameObject.WRAP):
            if(left):
                self.mX = self.mMaxX
            if(right):
                self.mX = self.mMinX
            if(up):
                self.mY = self.mMaxY
            if(down):
                self.mY = self.mMinY
        #If Action is STOP,BOUNCE, or DIE we correct position otherwise object
        #remains out of bounds
        else:
            if(left):
                self.mX = self.mMinX
            if(right):
                self.mX = self.mMaxX
            if(up):
                self.mY = self.mMinY
            if(down):
                self.mY = self.mMaxY

        if(self.mBoundAction == GameObject.STOP or self.mBoundAction == GameObject.DIE):
            self.mVelX = 0
            self.mVelY = 0
            
        elif(self.mBoundAction == GameObject.BOUNCE):
            if (left or right):
                self.mVelX *= -1
            if (up or down):
                self.mVelY *= -1
        if(self.mBoundAction == GameObject.DIE):
            self.mIsDead = True
            return
        
    def die(self):
        self.mIsDead = True
        
    def isDead(self):
        return self.mIsDead
    
    def setVelXY(self,aVelX,aVelY):
        self.mVelX = aVelX
        self.mVelY = aVelY

    def setVelX(self,aVelX):
        self.mVelX = aVelX

    def setVelY(self,aVelY):
        self.mVelY = aVelY

    def getVelX(self):
        return self.mVelX

    def getVelY(self):
        return self.mVelY
    
    def stopMove(self):
        self.mVelX = 0
        self.mVelY = 0
        self.mAccelX = 0
        self.mAccelY = 0
        
    def setAccel(self,aAccelX,aAccelY):
        self.mAccelX = self.aAccelX
        self.mAccelY = self.aAccelY
    
    def setXY(self,aX,aY):

        self.mX = aX
        self.mY = aY

    def setX(self,aX):
        self.mX = aX

    def setY(self,aY):
        self.mY = aY
        
    def setBounds(self,aMinX,aMaxX,aMinY,aMaxY):

        self.mMinX = aMinX
        self.mMaxX = aMaxX
        self.mMinY = aMinY
        self.mMaxY = aMaxY
        
    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getState(self):
        return self.mState

    def setState(self, aState):
        self.mState = aState
        self.mTimeState = 0

    def getTimeState(self):
        return self.mTimeState

    def update(self):
        self.mTimeState = self.mTimeState + 1
        self.mVelX = self.mVelX + self.mAccelX
        self.mVelY = self.mVelY + self.mAccelY
        self.mX += self.mVelX
        self.mY += self.mVelY
        self.checkBounds()
       
    def destroy(self):
        pass

        
    
