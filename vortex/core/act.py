class Act:

    def __init__(self, _database_obj, _ideas_obj_list):
        self._database = _database_obj
        self._ideas = _ideas_obj_list
        self._processed_ideas = list()

    def process(self):
        for idea in self._ideas:
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
        pass

    def display_results(self):
        for idea in self._processed_ideas:
            print('Idea Result '+str(idea.get_result()))