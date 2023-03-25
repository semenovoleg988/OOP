class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color


p1 = Point(10,20)
p2 = Point(12, 5, 'red')

points = [Point(x, x) for x in range(1, 2001, 2)]
points[1].color = 'yellow'
