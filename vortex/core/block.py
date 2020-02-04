import os

# this is the class that loads up a vdb file and operates it.


class Block:

    def __init__(self, _location, _data_directory, _data_key, _data_value):
        self._location = _location
        self._data_file_location = os.path.join(_data_directory, str(self._location) + '.vdb')
        self._data_file = None
        self._data_lines = None
        self._data_key = str(_data_key)
        self._data_value = str(_data_value)
        self._actual_count = 0
        if self._target_count == 0:
            if not os.path.isfile(self._data_file_location):
                open(self._data_file_location, 'x')

    def __del__(self):
        self._data_file.close()

    def write_data(self, data_key, data_value, data_set):
        self._data_file = open(self._data_file_location, 'a')
        self._data_file.write(str(data_key) + ':' + str(data_value) + '|' + self.create_data_string(data_set) + '\n')

    def read_data(self):
        self._data_file = open(self._data_file_location, 'r')
        self._data_lines = self._data_file.readlines()
        self._actual_count = len(self._data_lines)
        for line in self._data_lines:
            get_data_set = line.split('|')
            get_data_set_type = get_data_set[0].split(':')
            if self._data_key == get_data_set_type[0] and self._data_value == get_data_set_type[1]:
                get_data_set_data = get_data_set[1].split(',')
                for set_data in get_data_set_data:
                    data = set_data.split(':')
                    if data[0] == 'number':
                        self._actual_count += int(data[1])

    def create_data_string(self, data_set):
        data_string = ''
        for data_key, data_value in data_set.items():
            data_string += str(data_key) + ':' + str(data_value) + ','
        return data_string[:-1]

    def get_count(self):
        return self._actual_count

