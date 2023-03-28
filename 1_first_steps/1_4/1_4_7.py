import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(lst_values) != len(fields):
            return False

        for i, key in enumerate(fields):
            setattr(self, key, lst_values[i])
        return True

class StreamReader:
    FIELDS = ("id", "title", "pages")

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
    
sr = StreamReader()
data, result = sr.readlines()