import time


class Operation:

    def __init__(self):
        self.datetime_created = time.time()
        self.time_alive = 0

    def time_alive(self):
        self.time_alive = time.time() - self.datetime_created
        return self.time_alive
