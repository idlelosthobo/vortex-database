import os
from vortex.core import config


class Database:

    def __init__(self, _seek_file_location, _data_file_location):
        self._header_byte_size = 64
        self._seek_byte_size = 64
        self._seek_char_size = 3
        self._data_byte_size = config.data_size()
        self._seek_file_location = _seek_file_location
        self._data_file_location = _data_file_location
        self._header_length = len(config.file_header())
        self.database_ok = False
        if not os.path.isfile(_seek_file_location):
            try:
                open(_seek_file_location, 'x')
                new_seek_file = open(_seek_file_location, 'r+', encoding='utf-8')
                if self.check_header(new_seek_file, _seek_file_location):
                    self.build_new_seek(new_seek_file)
                    new_seek_file.close()
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

    def check_header(self, file, location):
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

    def get_data(self, value):
        pass

    def add_data(self, data_set):
        for data in data_set:
            for data_key, data_value in data.items():
                print('Data: ' + str(data_key) + ' ' + str(data_value))
                seek_byte_location = self.get_seek_location(str(data_value))
                print('Seek Byte: ' + str(seek_byte_location))
                self._seek.seek(seek_byte_location)
                print('"' + str(self._seek.read(seek_byte_location)))
        # self._data.write('hello')
        pass

    def read_seek(self):
        pass

    def write_seek(self):
        pass

    def get_seek_location(self, value):
        seek_location_byte = 0
        seek_value = value[:self._seek_char_size]
        if value.isnumeric():
            seek_int_value = 0
            for x in range(self._seek_char_size):
                if x < (self._seek_char_size - 1):
                    seek_int_value += 26 * (26 ** (self._seek_char_size - 1))
                else:
                    seek_int_value += 27
                if config.debug():
                    print(str(x) + ': ' + str(seek_int_value))
            for x in range(len(seek_value)):
                if x < (self._seek_char_size - 1):
                    seek_int_value += int(seek_value[x]) * (10 ** (self._seek_char_size - 1))
                else:
                    seek_int_value += int(seek_value[x])
                if config.debug():
                    print(str(x) + ': ' + str(seek_int_value))
            seek_location_byte = seek_int_value * self._seek_byte_size
            if config.debug():
                print("Seek Value: " + seek_value + ' ' + str(seek_int_value))
        else:
            seek_char_value = 0
            for x in range(len(seek_value)):
                if x < (self._seek_char_size - 1):
                    seek_char_value += (ord(seek_value[x]) - 97) * (26 ** (self._seek_char_size - 1))
                else:
                    seek_char_value += (ord(seek_value[x]) - 97)
                if config.debug():
                    print(str(x) + ': ' + str(seek_char_value))
            seek_location_byte = seek_char_value * self._seek_byte_size
            if config.debug():
                print("Seek Value: " + seek_value + ' ' + str(seek_char_value))
        return seek_location_byte + self._header_byte_size

    def build_new_seek(self, file):
        import itertools
        import string
        byte_location = self._header_byte_size
        seek_ascii_list = itertools.product(string.ascii_lowercase, repeat=self._seek_char_size)
        for seek_ascii_item in seek_ascii_list:
            file.seek(byte_location)
            file.write('0')
            file.seek(byte_location + (self._seek_byte_size / 2))
            file.write('0')
            byte_location += self._seek_byte_size
        seek_numbers_list = itertools.product('0123456789', repeat=self._seek_char_size)
        for seek_number_item in seek_numbers_list:
            file.seek(byte_location)
            file.write('0')
            file.seek(byte_location + (self._seek_byte_size / 2))
            file.write('0')
            byte_location += self._seek_byte_size
