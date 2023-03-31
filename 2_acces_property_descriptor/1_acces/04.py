class Money:
    def __init__(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money
        else:
            self.__money = 0

    def set_money(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn) -> None:
        self.__money += mn.get_money() 
    
    @classmethod
    def __check_money(cls, money) -> bool:
        return True if isinstance(money, int) and money >= 0 else False

m1 = Money(20)
m2 = Money(50)

m1.set_money(100)
m2.add_money(m1)

m1 = m1.get_money()
m2 = m2.get_money()

print(m1, m2)