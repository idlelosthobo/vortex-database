from ..nlp.memory import Memory


class Act:

    def __init__(self, _database_obj, _ideas_obj_list):
        self._database = _database_obj
        self._idea_list = _ideas_obj_list
        self._memory_list = list()
        self._processed_ideas = list()

    def process(self):
        for idea in self._idea_list:
            if idea.get_database_action() == 'store':
                self.store_idea(idea)
            elif idea.get_database_action() == 'retrieve':
                self.retrieve_from_idea(idea)
            print('Idea Processed '+str(idea.is_processed()))
            self._processed_ideas.append(idea)

    def store_idea(self, idea):
        self._database.store_data_set(idea.get_data_set())
        idea.set_result('Written to Database')

    def retrieve_from_idea(self, idea):
        memory = Memory(idea.get_data_set())
        memory.set_data_set_list(self._database.get_data(idea.get_data_set()))
        memory.debug_to_print()
        self._memory_list.append(memory)

    def display_results(self):
        for idea in self._processed_ideas:
            print('Idea Result '+str(idea.get_result()))
