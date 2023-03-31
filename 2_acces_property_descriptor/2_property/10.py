class PhoneNumber:
    def __init__(self, number, fio) -> None:
        self.number = number 
        self.fio = fio

class PhoneBook:
    def __init__(self) -> None:
        self.numbers = []

    def add_phone(self, phone: PhoneNumber):
        self.numbers.append(phone)

    def remove_phone(self, indx: int):
        self.numbers.pop(indx)

    def get_phone_list(self):
        return self.numbers
    
