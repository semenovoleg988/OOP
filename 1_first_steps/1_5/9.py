import sys

class ListObject:
    def __init__(self, data: str) -> None:
        self.next_obj = None
        self.data = data
    
    def link(self, obj):
        self.next_obj = obj

    def get_next(self):
        return self.next_obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
last_obj = head_obj
for i in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[i])
    last_obj.link(new_obj)
    last_obj = new_obj
del(last_obj)

"""next_object = head_obj
while True:
    print(next_object.data, next_object.next_obj)
    next_object = next_object.get_next()
    if next_object == None:
        break"""
