class AbstractClass:
    def __new__(cls) -> str:
        return "No way to create an object of this class"
    
obj = AbstractClass()
print(obj)