class CPU:
    def __init__(self, name: str, fr: int) -> None:
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name: str, cpu: CPU, mems: list[Memory]) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[0:self.total_mem_slots]

    def get_config(self) -> list:
        return [f'Материнська плата: {self.name}',
                f'Центральний процесор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотів пам\'яті: {self.total_mem_slots}',
                f'Пам\'ять: ', "; ".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]

