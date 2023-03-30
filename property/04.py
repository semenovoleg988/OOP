class Car:
    def __init__(self) -> None:
        self.__model = None

    @staticmethod
    def check_model(model):

        if not type(model) == str:
            return False
        
        if not 2 <= len(model) <= 100:
            return False
        
        return True

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.check_model(model):
            self.__model = model

    @model.deleter
    def model(self):
        del self.__model

car = Car()
print(car.__dict__)
car.model = "Ferrary"
print(car.__dict__)
del car.model
print(car.__dict__)
