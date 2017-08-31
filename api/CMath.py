import math

class CMath(object):

    def __init__(self):
        object.__init__(self)

    @classmethod
    def distance(cls,a,b):
        X = (a[0] - b[0])*(a[0] - b[0])
        Y = (a[1] - b[1])*(a[1] - b[1])
        dist = math.sqrt(X + Y)
        return dist

    @classmethod
    def sign(cls, a):
        if(a >= 0):
            return 1
        if (a < 0):
            return -1

    @classmethod
    def squareCollision(cls,x1,y1,w1,h1,x2,y2,w2,h2):
        if ((((x1 + w1) > x2) and (x1 < (x2 + w2))) and (((y1 + h1) > y2) and (y1 < (y2 + h2)))):
            return True
        else:
            return False