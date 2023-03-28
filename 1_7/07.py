from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name: str):
        if not (type(name) == str and 3 <= len(name) <= 50 and 
            set(name) < set(cls.CHARS_CORRECT)):
            raise ValueError("некорректное поле name")
        
    
    def __init__(self, name: str, size: int = 10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size
        

    def get_html(self):
        return f"<p class = 'login' > {self.name} < input type = 'text' size = {self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name: str):
        if not (type(name) == str and 3 <= len(name) <= 50 and
                set(name) < set(cls.CHARS_CORRECT)):
            raise ValueError("некорректное поле name")

    def __init__(self, name: str, size: int = 10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class = 'password' > {self.name} < input type = 'text' size = {self.size} />"


class FormLogin:
    def __init__(self, lgn: TextInput, psw: PasswordInput):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
