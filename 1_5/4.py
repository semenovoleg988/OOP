from random import randint

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = [(Line, Rect, Ellipse)[randint(0, 2)](randint(-100, 100), 2, 3, 4) for _ in range(217)]
for obj in elements:
    if isinstance(obj, Line):
        obj.ep = obj.sp = (0, 0)

print(*[elements[i].__dict__ for i in range(len(elements))], sep="\n")
