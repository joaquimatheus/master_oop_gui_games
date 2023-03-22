import math

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):
        if isinstance(oOther, Vector):
            return Vector((self.x * oOther.x), (self.y * oOther.y))
        elif isinstance(oOther, (int, float)):
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Second value must be a vector or scalar')
