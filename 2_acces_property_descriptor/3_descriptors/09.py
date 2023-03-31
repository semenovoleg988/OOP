class Thing:
    def __init__(self, name, weight) -> None:
        self.__name = name
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

class Bag:
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.__things = []
        self.weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if self.weight + thing.weight <= self.max_weight:
            self.things.append(thing)
            self.weight += thing.weight

    def get_total_weight(self):
        return self.weight
    
    def remove_thing(self, indx):
        self.weight -= self.things[indx].weight
        self.things.pop(indx)

bag = Bag(10000)
bag.add_thing(Thing("Python book", 100))
bag.add_thing(Thing("Good laptop", 500))
bag.add_thing(Thing("Solar panel", 4000))
bag.add_thing(Thing("Starlink", 5000))
w = bag.get_total_weight()
for thing in bag.things:
    print(f"{thing.name}: {thing.weight}")


print(f"Total weight: {w}")
