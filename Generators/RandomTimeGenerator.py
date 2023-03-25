import random
import datetime


class RandomTimeGenerator:
    dt = datetime.datetime.now()

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def next(self):
        self.dt = random.random() * (self.end - self.start) + self.start
        return self.dt.isoformat().replace("T", " ")

    def last(self):
        return self.dt.isoformat().replace("T", " ")
