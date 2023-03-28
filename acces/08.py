class Point:
    def __init__(self, x, y) -> None:
        self.__x, self.__y = x, y

    def get_coords(self):
        return self.__x, self.__y
    
class Rectangle:


    def draw(self):
        print(
            f"Прямокутник з координаами: {self.get_coords()[0]} {self.get_coords()[1]}")

    def __init__(self, *args):
        if len(args) == 2 and all(map(lambda x: type(x) == Point, args)):
            self.__sp = args[0] 
            print("Hi")
            self.__ep = args[1]
        elif len(args) == 4 and all(map(lambda x: type(x) in (int, float), args)):

            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep
    
    def get_coords(self):
        return self.__sp.get_coords(), self.__ep.get_coords()


rect = Rectangle(Point(0, 0), Point(20, 34))
rect.draw()