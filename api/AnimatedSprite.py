import pygame
from api.Sprite import *

class AnimatedSprite(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.mFrames = None
        self.mCurrentFrame = 0
        #Control counter of when to change the frame
        self.mTimeFrame = 0
        #How many frames must pass before changing the image
        self.mDelay = 0
        #Is animation cyclic or not
        self.mIsLoop = True
        #Has it ended?
        self.mEnded = False

    def initAnimation(self, aFramesArray, aStartFrame, aDelay, aIsLoop):
        self.mFrames = aFramesArray
        self.mCurrentFrame = aStartFrame
        self.mDelay = aDelay
        self.mIsLoop = aIsLoop
        self.mEnded = False
        self.setImage(self.mFrames[self.mCurrentFrame])
                
    def update(self):
        Sprite.update(self)
        #check if we need to change image
        self.mTimeFrame = self.mTimeFrame + 1
        if (self.mTimeFrame > self.mDelay):
            self.mTimeFrame = 0
            if (not self.mEnded):
                self.mCurrentFrame = self.mCurrentFrame + 1
                if (self.mCurrentFrame >= len (self.mFrames)):
                    if (self.mIsLoop):
                        self.mCurrentFrame = 0
                    else:
                        self.mCurrentFrame = len(self.mFrames)- 1
                        self.mEnded = True
                self.setImage(self.mFrames[self.mCurrentFrame])

    def isEnded(self):
        return self.mEnded

    def getCurrentFrame(self):
        return self.mCurrentFrame

    #Used to change animation speed
    def setDelay(self,aDelay):
        self.mDelay = aDelay
        
    def gotoAndStop(self,aFrame):
        if (aFrame >= 0 and aFrame <= (len(self.mFrames) - 1)):
            self.mCurrentFrame = aFrame
            self.setImage(self.mFrames[self.mCurrentFrame])
            self.mEnded = True

    def setState(self,aState):
        Sprite.setState(self,aState)
        
    def gotoAndPlay(self,aFrame):
        if (aFrame >= 0 and aFrame <= (len(self.mFrames) - 1)):
            self.mCurrentFrame = aFrame
            self.setImage(self.mFrames[self.mCurrentFrame])
            self.mEnded = False
            self.mTimeFrame = 0
            
    def render(self,aScreen):
        Sprite.render(self, aScreen)
        
    def destroy(self):     
        Sprite.destroy(self)
        i = len(self.mFrames)
        while (i > 0):
            self.mFrames[i - 1] = None
            self.mFrames.pop(i - 1)
            i -= 1
