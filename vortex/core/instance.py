import os
from vortex.config import INSTANCES_DIRECTORY


class Instance:

    def setup(self):
        if os.path.isdir(INSTANCES_DIRECTORY):
            if not os.path.isdir(self.instance_directory):
                os.mkdir(self.instance_directory)
        else:
            os.mkdir(INSTANCES_DIRECTORY)
            os.mkdir(self.instance_directory)

        print(self.name)

    def __init__(self, _name):
        self.name = _name
        self.run = True
        self.instance_directory = os.path.join(INSTANCES_DIRECTORY, str(self.name))
        self.setup()

    def input_as_str(self, value_str):
        if value_str == 'quit':
            self.run = False

    def result_as_str(self):
        pass

    def __bool__(self):
        return self.run
