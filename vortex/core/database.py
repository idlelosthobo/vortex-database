import os
from vortex.core import config


class Database:

    def __init__(self, _seek_file_location, _data_file_location):
        self._seek_file_location = _seek_file_location
        self._data_file_location = _data_file_location
        self._header_length = len(config.file_header())
        self.database_ok = False
        if not os.path.isfile(_seek_file_location):
            try:
                open(_seek_file_location, 'x')
            except:
                print('Failed to create seek file')

        if not os.path.isfile(_data_file_location):
            try:
                open(_data_file_location, 'x')
            except:
                print('Failed to create data file')

        self._seek = open(_seek_file_location, 'r+', encoding='utf-8')
        self._data = open(_data_file_location, 'r+', encoding='utf-8')
        self._seek_header_validated = self.check_header(self._seek, self._seek_file_location)
        self._data_header_validated = self.check_header(self._data, self._data_file_location)

        if self._seek_header_validated and self._data_header_validated:
            self.database_ok = True

        if config.debug():
            print('Database Ok: ' + str(self.database_ok))
            print(self.build_new_seek(self._seek))

    def check_header(self, file, location):
        header_validated = False
        if os.stat(location).st_size == 0:
            file.seek(0)
            file.write(config.file_header())
            file.seek(0)
            header = file.read(self._header_length)
            header_validated = True
        else:
            file.seek(0)
            header = file.read(self._header_length)
            if header == config.file_header():
                header_validated = True
            else:
                header_validated = False
        if config.debug():
            print('Database ' + str(location) + ' Header: ' + header)
            print('Database ' + str(location) + ' Header Validated: ' + str(header_validated))
        return header_validated

    def get_data(self, _location, _length):
        pass

    def add_data(self, data_set):
        self._data.write('hello')
        pass

    def read_seek(self):
        pass

    def write_seek(self):
        pass

    def build_new_seek(self, file):
        import itertools
        import string
        byte_location = 64
        byte_size = 64
        seek_ascii_list = itertools.product(string.ascii_lowercase, repeat=3)
        for seek_ascii_item in seek_ascii_list:
            file.seek(byte_location)
            file.write('0')
            file.seek(byte_location + 32)
            file.write('0')
            byte_location += byte_size
        seek_numbers_list = itertools.product('0123456789', repeat=3)
        for seek_number_item in seek_numbers_list:
            file.seek(byte_location)
            file.write('0')
            file.seek(byte_location + 32)
            file.write('0')
            byte_location += byte_size
