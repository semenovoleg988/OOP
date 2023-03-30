class StackObj:
    def __init__(self, data: str) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self): return self.__data
    @data.setter
    def data(self, data): self.__data = data
    @property
    def next(self): return self.__next
    @next.setter
    def next(self, next):
        if type(next) in (StackObj, type(None)): self.__next = next

class Stack: 
    def __init__(self) -> None: self.top = None

    def push(self, obj: StackObj):
        if self.top == None:
            self.top = obj
            return
        
        tail = self.top
        while tail.next != None:
            tail = tail.next
        else:
            tail.next = obj

    def pop(self):
        if self.top == None: return
        
        tail = self.top
        if tail.next == None: 
            self.top = None
            return tail
        
        while tail.next.next != None:
            tail = tail.next
        else:
            result = tail.next
            tail.next = None
            return result

    def get_data(self):
        if self.top == None: return []
        tail = self.top
        result = [tail.data]
        if tail.next == None:
            return result
        while tail.next != None:
            tail = tail.next
            result.append(tail.data)
        return result

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.push(StackObj("obj4"))
st.push(StackObj("obj5"))
st.pop()
print(st.get_data())
