import os
from ..settings import INSTANCES_DIRECTORY
from ..api.string import process
from ..nlp.thought import Thought
from ..loc.locale import Locale
from vortex.data.database import Database
from ..core.act import Act


class Instance:

    def __init__(self, _name):
        self.name = _name
        self.run = True
        self.instance_directory = os.path.join(INSTANCES_DIRECTORY, str(self.name))
        self.data_directory = os.path.join(self.instance_directory, 'data')
        self.seek_file_location = os.path.join(self.instance_directory, 'seek.vsf')
        self.seek = None
        self.data = None
        self.Thought = None
        self.Locale = None
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
        self.Locale = Locale()
        self.Locale.print_words()

    def input_as_string(self, value_str):
        self.Thought = Thought(process(value_str))
        ideas = self.Locale.thought_to_ideas(self.Thought)
        act = Act(self.data, ideas)
        act.process()
        act.display_results()
        # self.Thought.process()
        # self.data.process_data(self.Thought.get_data_set())
        if value_str == 'quit':
            self.run = False

    def result_as_string(self):
        return self.Thought.get_data_set()

    def __bool__(self):
        return self.run
