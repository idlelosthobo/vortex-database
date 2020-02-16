class Idea:

    def __init__(self, _database_action, _data_set):
        if _database_action == 'store' or 'retrieve':
            self._database_action = _database_action
        self._data_set = _data_set

    def get_database_action(self):
        return self._database_action

    def get_data_set(self):
        return self._data_set
