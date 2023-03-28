class Factory:
    @staticmethod
    def build_sequence() -> list:
        return []

    @staticmethod
    def build_number(sub: str) -> int:
        return int(sub)

class Loader:
    @staticmethod
    def parse_format(string: str, factory: Factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
