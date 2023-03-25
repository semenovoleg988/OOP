from typing import Union

class Table:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Cart:
    def __init__(self) -> None:
        self.goods = []

    def add(self, gd: Union[Table, TV, Notebook, Cup]):
        self.goods.append(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def getlist(self):
        return list(map(lambda x: x.name + ": " + x.price, self.goods))
    
cart = Cart()

cart.add(TV("Samsung", '5000'))
cart.add(TV("HP", '4000'))
cart.add(Table("Jysk", '3000'))
cart.add(Notebook("Apple", '50000'))
cart.add(Notebook("Lenovo", '40000'))
cart.add(Cup("Glass", '50'))
cart.remove(3)

print(cart.getlist())