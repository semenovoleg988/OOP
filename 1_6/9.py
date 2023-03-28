from typing import Self

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def clone(self):
        return Point(self.x, self.y)
    
pt = Point(1, 2)
pt2 = pt.clone()

print(pt.__dict__)
print(pt2.__dict__)