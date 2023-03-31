class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if not type(value) in (int, float):
            raise TypeError("Should be intor float")
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()
    def __init__(self, value = 0.0) -> None:
        self.value = value

class Table:
    def __init__(self, N, M) -> None:
        self.cells = [[Cell() for _ in range(M)] for __ in range(N)]

table = Table(5, 3)
i = 1
for line in table.cells:
    for c in line:
        c.value = i
        i += 1

for line in table.cells:
    for c in line:
        print(c.value, end=" ")
    print()
