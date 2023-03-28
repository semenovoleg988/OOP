class Message:
    def __init__(self, text: str) -> None:
        self.text = text
        self.fl_like = False


class Viber:
    msgs = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.msgs.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.msgs.remove(msg)

    @classmethod
    def set_like(cls, msg: Message):
        cls.msgs[cls.msgs.index(msg)].fl_like = True

    @classmethod
    def show_last_message(cls, number: int):
        return cls.msgs[-1:-6:-1]

    @classmethod
    def total_message(cls):
        return len(cls.msgs)
