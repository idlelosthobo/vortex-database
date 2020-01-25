import time


class Operation:

    def __init__(self):
        self.datetime_created = 0.0
        self.time_alive = 0.0
        self.datetime_created = (time.time() * 1000000000)

    def get_time_alive(self):
        self.time_alive = (time.time() * 1000000000) - self.datetime_created
        return self.time_alive
