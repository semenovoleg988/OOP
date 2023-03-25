import sys

class Database:
    lst_data = []
    Fields = ("id", "name", "old", "salary")

    def select(self, a, b):
        return self.lst_data[a, b+1]
    
    def insert(self, data):
        for element in data:
            self.lst_data.append(dict(zip(self.Fields, element.split())))


lst_in = list(map(str.strip, sys.stdin.readlines()))
