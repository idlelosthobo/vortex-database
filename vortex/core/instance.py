import os
from ..settings import INSTANCES_DIRECTORY
from ..api.string import process
from ..nlp.thought import Thought
from ..db.data import Data


class Instance:

    def setup(self):
        if os.path.isdir(INSTANCES_DIRECTORY):
            if not os.path.isdir(self.instance_directory):
                os.mkdir(self.instance_directory)
        else:
            os.mkdir(INSTANCES_DIRECTORY)
            os.mkdir(self.instance_directory)

        if not os.path.isfile(self.seek_file_location):
            open(self.seek_file_location, 'x')

        if not os.path.isfile(self.data_file_location):
            open(self.data_file_location, 'x')

        self.data = Data(self.seek_file_location, self.data_file_location)

        print(self.name)

    def __init__(self, _name):
        self.name = _name
        self.run = True
        self.instance_directory = os.path.join(INSTANCES_DIRECTORY, str(self.name))
        self.seek_file_location = os.path.join(self.instance_directory, 'seek.vdb')
        self.data_file_location = os.path.join(self.instance_directory, 'data.vdb')
        self.seek = None
        self.data = None
        self.thought = None
        self.setup()

    def input_as_string(self, value_str):
        self.thought = Thought(process(value_str))
        self.thought.process()
        print(self.thought.get_data_set())
        if value_str == 'quit':
            self.run = False

    def result_as_string(self):
        pass

    def __bool__(self):
        return self.run
