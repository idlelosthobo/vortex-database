import os
from ..core.dataset import DataSet
# this is the class that loads up a vdb file and operates it.


class Block:

    def __init__(self, _location, _data_directory, _data_count):
        self._location = _location
        self._data_file_location = os.path.join(_data_directory, str(self._location) + '.vdb')
        self._data_file = None
        self._data_lines = None
        self._data_set_list = list()
        self._data_count = _data_count
        if self._data_count == 0:
            if not os.path.isfile(self._data_file_location):
                open(self._data_file_location, 'x')

    def write_data(self, data_key, data_value, data_set_str):
        self._data_file = open(self._data_file_location, 'a')
        self._data_file.write(str(data_key) + ':' + str(data_value) + '|' + str(data_set_str) + '\n')

    def read_data(self, data_key, data_value):
        self._data_file = open(self._data_file_location, 'r')
        self._data_lines = self._data_file.readlines()
        self._data_count = len(self._data_lines)
        for line in self._data_lines:
            get_data_set = line.split('|')
            get_data_set_type = get_data_set[0].split(':')
            if data_key == get_data_set_type[0] and data_value == get_data_set_type[1]:
                get_data_set_data = get_data_set[1].split(',')
                for set_data in get_data_set_data:
                    data = set_data.split(':')
                    data_set = DataSet()
                    data_set.add_data_item(data[0], data[1])
                    print('Get: Key: ' + data[0])
                    print('Get: Value: ' + data[1])
                    # print('Get: Number Count: ' + str(number_count))
                self._data_set_list.append(data_set)

    def get_count(self):
        return self._data_count

    def get_data_set_list(self):
        return self._data_set_list
