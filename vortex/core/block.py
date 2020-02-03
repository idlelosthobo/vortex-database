import os

# this is the class that loads up a vdb file and operates it.


class Block:

    def __init__(self, _location, _data_directory):
        self._location = _location
        self._data_directory = _data_directory
        self._data = None

    def open_file(self):
        data_file_location = os.path.join(self._data_directory, str(self._location) + '.vdb')
        data_file = open(data_file_location, 'r')


