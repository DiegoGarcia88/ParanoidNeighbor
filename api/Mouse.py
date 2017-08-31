import pygame

class Mouse(object):
    mInstance = None
    mInitialized = False
    mLeftPressed = False
    mRightPressed = False
    mCenterPressed = False
    mLeftPressedPreviousFrame = False
    mRightPressedPreviousFrame = False
    def __new__(self,*args,**kargs):
        if(Mouse.mInstance is None):
            Mouse.mInstance = object.__new__(self,*args,**kargs)
            self.init(Mouse.mInstance)
        else:
            print("Careful: Mouse(): You shouldn't instance this class more than once. Use Mouse.inst()")
        return Mouse.mInstance
    @classmethod

    def inst(cls):
        if(not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (Mouse.mInitialized):
            return
        Mouse.mInitialized = True
        Mouse.mLeftPressed = False
        Mouse.mRightPressed = False
        Mouse.mCenterPressed = False
        Mouse.mLeftPressedPreviousFrame = False
        Mouse.mRightPressedPreviousFrame = False

    def update(self):
        Mouse.mLeftPressedPreviousFrame = Mouse.mLeftPressed
        Mouse.mRightPressedPreviousFrame = Mouse.mRightPressed
        Mouse.mLeftPressed = pygame.mouse.get_pressed()[0]
        Mouse.mRightPressed = pygame.mouse.get_pressed()[2]
        Mouse.mCenterPressed = pygame.mouse.get_pressed()[1]
        
    def leftPressed(self):
        return Mouse.mLeftPressed

    def rightPressed(self):
        return Mouse.mRightPressed

    def centerPressed(self):
        return Mouse.mCenterPressed

    def fire(self):
        return Mouse.mLeftPressed == True and Mouse.mLeftPressedPreviousFrame == False

    def reload(self):
        return Mouse.mRightPressed == True and Mouse.mRightPressedPreviousFrame == False

    def click(self):
        return Mouse.mLeftPressed == False and Mouse.mLeftPressedPreviousFrame == True

    def getPos(self):
        return pygame.mouse.get_pos()

    def getX(self):
        return pygame.mouse.get_pos()[0]

    def getY(self):
        return pygame.mouse.get_pos()[1]

    def destroy(self):
        Mouse.mInstance = None
