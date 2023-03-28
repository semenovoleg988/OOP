class Factory:
    def build_sequence(self) -> list:
        return []

    def build_number(self, string):
        return int(string)

class Loader:
    def parse_format(self, string: str, factory: Factory) -> list:
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
