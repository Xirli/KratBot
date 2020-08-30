from time import time


class Action:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.time_end = time() + duration
