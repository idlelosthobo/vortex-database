from vortex.data.dataset import DataSet
from ..core import config


class Idea:

    def __init__(self):
        self._store_weight = 0
        self._retrieve_weight = 0
        self._database_action = None
        self._data_set = DataSet()
        self._data_set.add_data_item('time_entered', config.time_now())
        self._processed = False
        self._result = None

    def evaluate_action(self, action):
        if action == 'store':
            self._store_weight += 1
        elif action == 'retrieve':
            self._retrieve_weight += 1
        if self._store_weight > self._retrieve_weight:
            self._database_action = 'store'
        elif self._retrieve_weight > self._store_weight:
            self._database_action = 'retrieve'
        else:
            self._database_action = None

    def has_database_action(self):
        if self._database_action == 'store' or 'retrieve':
            return True
        else:
            return False

    def get_database_action(self):
        return self._database_action

    def add_data(self, key, value):
        self._data_set.add_data_item(key, value)

    def get_data_set(self):
        return self._data_set

    def set_processed(self):
        self._processed = True

    def is_processed(self):
        return self._processed

    def set_result(self, result=''):
        self._result = result

    def get_result(self):
        return self._result
