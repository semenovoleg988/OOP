class RadiusVector2D:
    MIN_COORD, MAX_COORD = -100, 1024
    def __init__(self, x: int=0, y: int=0) -> None:
        self.__x, self.__y = 0, 0
        self.x, self.y = x, y

    @staticmethod
    def norm2(vector): 
        return vector.x**2 + vector.y**2

    @classmethod
    def check_value(cls, value): 
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x): 
        if self.check_value(x):self.__x = x
    @property
    def y(self): 
        return self.__y
    @y.setter
    def y(self, y): 
        if self.check_value(y): self.__y = y
