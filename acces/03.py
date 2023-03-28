class Clock:
    @staticmethod
    def __check_time(tm) -> bool:
        if type(tm) == int and 0 <= tm < 1000:
            return True
        return False

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm


    def __init__(self, tm = 0) -> None:
        if self.__check_time(tm):
            self.__time = tm
        else:
            self.__time = 0
    def get_time(self):
        print(self.__time)

clock = Clock(450)
clock.set_time(500)
clock.get_time()

