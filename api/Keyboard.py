import pygame

class Keyboard(object):
    mInstance = None
    mInitialized = False
    mLeftPressed = False
    mRightPressed = False
    mSpacePressed = False
    mSpacePressedPreviousFrame = False
    mAPressed = False
    mBPressed = False
    mBPressedPreviousFrame = False
    mCPressed = False
    mCPressedPreviousFrame = False
    mDPressed = False
    mEPressed = False
    mFPressed = False
    mGPressed = False
    mHPressed = False
    mHPressedPreviousFrame = False
    mIPressed = False
    mIPressedPreviousFrame = False
    mJPressed = False
    mKPressed = False
    mLPressed = False
    mMPressed = False
    mNPressed = False
    mOPressed = False
    mPPressed = False
    mPPressedPreviousFrame = False
    mQPressed = False
    mQPressedPreviousFrame = False
    mRPressed = False
    mRPressedPreviousFrame = False
    mSPressed = False
    mSPressedPreviousFrame = False
    mTPressed = False
    mUPressed = False
    mVPressed = False
    mWPressed = False
    mXPressed = False
    mYPressed = False
    mZPressed = False
    mEnterPressed = False
    mEnterPressedPreviousFrame = False

    def __new__(self,*args,**kargs):
        if (Keyboard.mInstance is None):
            Keyboard.mInstance = object.__new__(self, *args,**kargs)
            self.init(Keyboard.mInstance)
        else:
            print("Careful: Keyboard(): This class shouldn't be instanced more than once. Use Keyboard.inst().")
        return Keyboard.mInstance
    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    def init(self):
        if(Keyboard.mInitialized):
            return
        Keyboard.mInitialized = True
        Keyboard.mLeftPressed = False
        Keyboard.mRightPressed = False
        Keyboard.mSpacePressed = False
        Keyboard.mAPressed = False
        Keyboard.mBPressed = False
        Keyboard.mBPressedPreviousFrame = False
        Keyboard.mCPressed = False
        Keyboard.mCPressedPreviousFrame = False
        Keyboard.mDPressed = False
        Keyboard.mEPressed = False
        Keyboard.mFPressed = False
        Keyboard.mGPressed = False
        Keyboard.mHPressed = False
        Keyboard.mHPressedPreviousFrame = False
        Keyboard.mIPressed = False
        Keyboard.mIPressedPreviousFrame = False
        Keyboard.mJPressed = False
        Keyboard.mKPressed = False
        Keyboard.mLPressed = False
        Keyboard.mMPressed = False
        Keyboard.mNPressed = False
        Keyboard.mOPressed = False
        Keyboard.mPPressed = False
        Keyboard.mPPressedPreviousFrame = False
        Keyboard.mQPressed = False
        Keyboard.mQPressedPreviousFrame = False
        Keyboard.mRPressed = False
        Keyboard.mRPressedPreviousFrame = False
        Keyboard.mSPressed = False
        Keyboard.mSPressedPreviousFrame = False
        Keyboard.mTPressed = False
        Keyboard.mUPressed = False
        Keyboard.mVPressed = False
        Keyboard.mWPressed = False
        Keyboard.mXPressed = False
        Keyboard.mYPressed = False
        Keyboard.mZPressed = False
        Keyboard.mEnterPressed = False
        Keyboard.mEnterPressedPreviousFrame = False

    def update(self):
        Keyboard.mSpacePressedPreviousFrame = Keyboard.mSpacePressed
        Keyboard.mEnterPressedPreviousFrame = Keyboard.mEnterPressed
        Keyboard.mBPressedPreviousFrame = Keyboard.mBPressed
        Keyboard.mCPressedPreviousFrame = Keyboard.mCPressed
        Keyboard.mIPressedPreviousFrame = Keyboard.mIPressed
        Keyboard.mPPressedPreviousFrame = Keyboard.mPPressed
        Keyboard.mQPressedPreviousFrame = Keyboard.mQPressed
        Keyboard.mRPressedPreviousFrame = Keyboard.mRPressed
        Keyboard.mSPressedPreviousFrame = Keyboard.mSPressed
        Keyboard.mHPressedPreviousFrame = Keyboard.mHPressed

    #Player 1 fire
    def fire(self):
        return Keyboard.mSpacePressed == True and Keyboard.mSpacePressedPreviousFrame == False

    #Player 2 fire
    def fire2(self):
        return Keyboard.mQPressed == True and Keyboard.mQPressedPreviousFrame == False
    
    def keyDown(self, aKey):
        if (aKey == pygame.K_LEFT):
            Keyboard.mLeftPressed = True
        if (aKey == pygame.K_RIGHT):
            Keyboard.mRightPressed = True
        if (aKey == pygame.K_SPACE):
            Keyboard.mSpacePressed = True
        if (aKey == pygame.K_a):
            Keyboard.mAPressed = True
        if (aKey == pygame.K_b):
            Keyboard.mBPressed = True
        if (aKey == pygame.K_c):
            Keyboard.mCPressed = True
        if (aKey == pygame.K_d):
            Keyboard.mDPressed = True
        if (aKey == pygame.K_h):
            Keyboard.mHPressed = True
        if (aKey == pygame.K_i):
            Keyboard.mIPressed = True
        if (aKey == pygame.K_p):
            Keyboard.mPPressed = True
        if (aKey == pygame.K_q):
            Keyboard.mQPressed = True
        if (aKey == pygame.K_r):
            Keyboard.mRPressed = True
        if (aKey == pygame.K_s):
            Keyboard.mSPressed = True
        if (aKey == pygame.K_RETURN):
            Keyboard.mEnterPressed = True

    def keyUp(self,aKey):
        if (aKey == pygame.K_LEFT):
            Keyboard.mLeftPressed = False
        if (aKey == pygame.K_RIGHT):
             Keyboard.mRightPressed = False
        if (aKey == pygame.K_SPACE):
            Keyboard.mSpacePressed = False
        if (aKey == pygame.K_a):
            Keyboard.mAPressed = False
        if (aKey == pygame.K_b):
            Keyboard.mBPressed = False
        if (aKey == pygame.K_c):
            Keyboard.mCPressed = False
        if (aKey == pygame.K_d):
            Keyboard.mDPressed = False
        if (aKey == pygame.K_h):
            Keyboard.mHPressed = False
        if (aKey == pygame.K_i):
            Keyboard.mIPressed = False
        if (aKey == pygame.K_p):
            Keyboard.mPPressed = False
        if (aKey == pygame.K_q):
            Keyboard.mQPressed = False
        if (aKey == pygame.K_r):
            Keyboard.mRPressed = False
        if (aKey == pygame.K_s):
            Keyboard.mSPressed = False
        if (aKey == pygame.K_RETURN):
            Keyboard.mEnterPressed = False
        
    def leftPressed(self):
        return Keyboard.mLeftPressed

    def rightPressed(self):
        return Keyboard.mRightPressed
    
    def spacePressed(self):
        return Keyboard.mSpacePressed

    def EnterPressed(self):
        return Keyboard.mEnterPressed

    def APressed(self):
        return Keyboard.mAPressed

    def BPressed(self):
        return Keyboard.mAPressed

    def CPressed(self):
        return Keyboard.mAPressed

    def DPressed(self):
        return Keyboard.mDPressed

    def HPressed(self):
        return Keyboard.mHPressed

    def IPressed(self):
        return Keyboard.mAPressed

    def PPressed(self):
        return Keyboard.mPPressed

    def QPressed(self):
        return Keyboard.mQPressed

    def RPressed(self):
        return Keyboard.mRPressed

    def SPressed(self):
        return Keyboard.mSPressed

    def pauseKey(self):
        return (Keyboard.mPPressed == True and Keyboard.mPPressedPreviousFrame == False) or (Keyboard.mEnterPressed == True and Keyboard.mEnterPressedPreviousFrame == False)

    def bKey(self):
        return (Keyboard.mBPressed == True and Keyboard.mBPressedPreviousFrame == False)

    def cKey(self):
        return (Keyboard.mCPressed == True and Keyboard.mCPressedPreviousFrame == False)

    def hKey(self):
        return (Keyboard.mHPressed == True and Keyboard.mHPressedPreviousFrame == False)

    def iKey(self):
        return (Keyboard.mIPressed == True and Keyboard.mIPressedPreviousFrame == False)

    def pKey(self):
        return (Keyboard.mPPressed == True and Keyboard.mPPressedPreviousFrame == False)

    def rKey(self):
        return (Keyboard.mRPressed == True and Keyboard.mRPressedPreviousFrame == False)

    def sKey(self):
        return (Keyboard.mSPressed == True and Keyboard.mSPressedPreviousFrame == False)

    def destroy(self):
        Keyboard.mInstance = None
