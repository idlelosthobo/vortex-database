

class Memory:

    def __init__(self, _context_data_set):
        self._data_set_list = list()
        self._context_data_set = _context_data_set

    def add_data_set(self, data_set_obj):
        self._data_set_list.append(data_set_obj)

    def set_data_set_list(self, data_set_list):
        self._data_set_list = data_set_list

    def get_data_set_list(self):
        return self._data_set_list
