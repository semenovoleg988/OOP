class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __init__(self, min_length=2, max_length=50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if (type(value) == str and 
                self.min_length <= len(value) <= self.max_length):
            setattr(instance, self.name, value)

class PriceValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __init__(self, max_value=10000) -> None:
        self.max_value = max_value

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if (type(value) in (int, float) and
            0 <= value <= self.max_value):
            setattr(instance, self.name, value)

class Product:
    name = StringValue()
    price = PriceValue()
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product:Product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

shop = SuperShop("Semenov`s shop")
shop.add_product(Product("Flashlight", 700))
shop.add_product(Product("Radio", 1000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
