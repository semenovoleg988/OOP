from string import ascii_letters, digits
from random import randint

class EmailValidator:
    def __new__(cls):
        return None
    
    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False

    @classmethod
    def get_random_email(cls) -> str:
        AVAILABLE = ascii_letters  + "_"
        AV_len = len(AVAILABLE) - 1
        return "".join(AVAILABLE[randint(0, AV_len)] for _ in range(randint(10, 15))) + "@gmail.com"

    @classmethod
    def check_email(cls, email: str) -> bool:
        AVAILABLE = set(ascii_letters + digits + "_" + ".")

        if not cls.__is_email_str(email): 
            return False
        
        if email.count("@") == 1:
            parts = email.split("@")
            if (len(parts[0]) <= 100 and len(parts[1]) <= 50 and 
                set(parts[0]) < AVAILABLE and set(parts[1]) < AVAILABLE and
                "." in parts[1] and not ".." in email):
                return True
        return False


print(EmailValidator.check_email("semenovoleg988@gmail.com"))

for _ in range(50):
    print(EmailValidator.get_random_email())
