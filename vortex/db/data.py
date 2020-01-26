import time
class Data:

    def __init__(self, _seek_file_path, _data_file_path):
        self._file_seek = open(_seek_file_path, 'rb+')
        self._file_data = open(_data_file_path, 'rb+')

    def get_data(self, _location, _length):
        pass

    def add_data(self, _iteration=time.time()):
        pass
