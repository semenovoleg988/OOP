class ValidateString:
    def __init__(self, min_length = 3, max_length = 100) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) == str and self.min_length <= len(string) <= self.max_length:
            return True
        else:
            return False
        

class StringValue:
    def __set_name__(self, owner, name, validator: ValidateString = ValidateString()):
        self.name = "_" + name
        self.validator = validator

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)
    

class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()
    
    def __init__(self, login, password, email) -> None:
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]
    
    def show(self):
        print(f"<form>\nLogin: {self.login}\nPassword: {self.password}\nEmail: {self.email}\n</form>")




form = RegisterForm("semenovoleg", "12345", "semen@gmail.com")

print(form.get_fields())
form.show()
print(form.__dict__)