class TeleCast:
    def __init__(self, id: int, name: str, duration: int) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, telecast_id):
        map(lambda x: self.items.pop(x), [i for i in range(len(self.items)) if self.items[i].uid == telecast_id])