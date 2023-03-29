class ObjList:
    def __init__(self, data) -> None:
        self.__next = self.__prev = None
        self.__data = data

    def set_next(self, obj) -> None:
        self.__next = obj

    def set_prev(self, obj) -> None:
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data) -> None:
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    @staticmethod
    def link(first: ObjList, second: ObjList):
        first.set_next(second)
        second.set_prev(first)

    def __init__(self) -> None:
        self.head = self.tail = None

    def add_obj(self, obj: ObjList):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.link(self.tail, obj)
            self.tail = obj
        
    def remove_obj(self):
        if self.tail == None or self.tail.get_prev() == None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()

    def get_data(self):
        if self.head:
            arr = [self.head]
            print(arr)
            while arr[-1].get_next():
                print(arr)

                arr.append(arr[-1].get_next())
            arr = [x.get_data() for x in arr]
        return arr

lst = LinkedList()
lst.add_obj(ObjList(1))
lst.add_obj(ObjList(2))
lst.add_obj(ObjList(3))
lst.add_obj(ObjList(4))
lst.remove_obj()
lst.add_obj(ObjList(5))
print(lst.get_data())
