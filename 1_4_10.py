class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]
    
tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобіль")
tr.add("leaf", "лист")
tr.add("river", "річка")
tr.add("go", "йти")
tr.add("go", "їхати")
tr.add("go", "ходити")
tr.add("milk", "молоко")

tr.remove("car")

print(*tr.translate("go"))
