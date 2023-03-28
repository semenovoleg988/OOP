from string import ascii_uppercase, digits

class CardCheck:
    @staticmethod
    def check_card_number(number: str):
        numb_list = number.split("-")
        if len(numb_list) != 4:
            return False 
        for four in numb_list:
            if not(len(four) == 4 and set(four) < set(digits)):
                return False
        return True
    
    @staticmethod
    def check_name(name: str):
        if len(name.split(" ")) != 2 or not(set(name.replace(" ", "")) < set(ascii_uppercase)):
            return False
        
        return True

print(CardCheck.check_card_number("1234-1234-1234-1234"))

print(CardCheck.check_name("OLEG SEMENOV"))