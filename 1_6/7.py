class SingletonFive:
    _n = 0
    _singleton = None
    def __new__(cls, *arg):
        if cls._n < 5:
            cls._n += 1
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __init__(self, name: str) -> None:
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
print(*map(lambda x: x.name, objs))