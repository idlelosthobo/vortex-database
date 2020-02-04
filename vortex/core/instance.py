import os
from ..settings import INSTANCES_DIRECTORY
from ..api.string import process
from ..nlp.thought import Thought
from vortex.core.database import Database


class Instance:

    def __init__(self, _name):
        self.name = _name
        self.run = True
        self.instance_directory = os.path.join(INSTANCES_DIRECTORY, str(self.name))
        self.data_directory = os.path.join(self.instance_directory, 'data')
        self.seek_file_location = os.path.join(self.instance_directory, 'seek.vsf')
        self.seek = None
        self.data = None
        self.thought = None
        self.setup()

    def setup(self):
        if os.path.isdir(INSTANCES_DIRECTORY):
            if not os.path.isdir(self.instance_directory):
                os.mkdir(self.instance_directory)
                os.mkdir(self.data_directory)
            else:
                if not os.path.isdir(self.data_directory):
                    os.mkdir(self.data_directory)

        else:
            os.mkdir(INSTANCES_DIRECTORY)
            os.mkdir(self.instance_directory)
            os.mkdir(self.data_directory)

        self.data = Database(self.seek_file_location, self.data_directory)

    def input_as_string(self, value_str):
        self.thought = Thought(process(value_str))
        self.thought.process()
        self.data.process_data(self.thought.get_data_set())
        if value_str == 'quit':
            self.run = False

    def result_as_string(self):
        return self.thought.get_data_set()

    def __bool__(self):
        return self.run
