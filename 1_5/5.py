class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float) and x > 0, (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x*2 < self.a + self.b + self.c, (self.a, self.b, self.c))):
            return 2
        return 3
    
a, b, c = map(int, input().split())
while a*b*c != 0:
    tr = TriangleChecker(a, b, c)

    print(tr.is_triangle())
    a, b, c = map(int, input().split())
