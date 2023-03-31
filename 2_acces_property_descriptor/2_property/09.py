from math import sqrt

class LineTo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

class PathLines:
    def __init__(self, *args) -> None:
        self.arr = list(args)

    def get_path(self):
        return self.arr
    
    @staticmethod
    def __length(obj1: LineTo, obj2: LineTo):
        dx = obj2.x - obj1.x
        dy = obj2.y - obj1.y
        return sqrt(dx**2 + dy**2)

    def get_legth(self):
        arr = self.arr
        length = self.__length

        if not arr:
            return []
        summa = length(LineTo(0,0), arr[0])
        for i in range(1, len(arr)):
            summa += length(arr[i-1], arr[i])
        return summa
    
    def add_line(self, line: LineTo):
        self.arr.append(line)
    
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dest = p.get_legth()
print(dest)