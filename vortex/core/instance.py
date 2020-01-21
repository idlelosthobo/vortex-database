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
        self.instance_directory = os.path.join(INSTANCES_DIRECTORY, str(self.name))
        self.setup()

