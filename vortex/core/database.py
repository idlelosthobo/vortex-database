import os
from vortex.core import config


class Database:

    def __init__(self, _seek_file_location, _data_directory):
        self._header_byte_size = 64
        self._seek_byte_size = 32
        self._seek_char_size = 3
        self._seek_file_location = _seek_file_location
        self._data_directory = _data_directory
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

        if os.path.isdir(_data_directory):
            print('Failed to find data directory')
            self._data_directory_validated = False
        else:
            print('Directory found')
            self._data_directory_validated = True
        self._seek = open(_seek_file_location, 'r+', encoding='utf-8')
        self.build_new_seek(self._seek)
        self._seek_header_validated = self.check_header(self._seek, self._seek_file_location)

        if self._seek_header_validated and self._data_directory_validated:
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

    def process_data(self, data_set):
        print(list(data_set))
        for data in data_set:
            print(list(data))
            if data['data_set_type'] == 'input':
                self.add_data(dict(data['data']))

    def get_data(self, value):
        seek_location = self.get_seek_location(value)
        data_count = self.read_seek_count(seek_location)
        if data_count >= 0:
            data_file_location = os.path.join(self._data_directory, str(seek_location) + '.vdb')
            data_file = open(data_file_location, 'r')
            for x in range(data_count):
                data_set = data_file.readline(x).split('|')
                for data_key, data_value in data_set:
                    print('Get Data: Key: ' + data_key + ' Value: ' + data_value)
        else:
            print('No data available on this request')
        pass

    def create_data_string(self, data_set):
        data_string = ''
        for data_key, data_value in data_set.items():
            data_string += str(data_key) + ':' + str(data_value) + ','
        return data_string[:-1]

    def add_data(self, data_set):
        for data_key, data_value in data_set.items():
            print('Data: ' + str(data_key) + ' ' + str(data_value))
            seek_location = self.get_seek_location(str(data_value))
            print('Seek Byte: ' + str(seek_location * self._seek_byte_size))
            data_count = self.read_seek_count(seek_location)
            self._seek.seek(seek_location * self._seek_byte_size)
            print('"' + str(self._seek.read(self._seek_byte_size)) + '"')
            print('Data Count: ' + str(data_count))
            data_file_location = os.path.join(self._data_directory, str(seek_location) + '.vdb')
            if data_count == 0:
                if not os.path.isfile(data_file_location):
                    open(data_file_location, 'x')
            data_file = open(data_file_location, 'a')
            data_file.write(str(data_key) + ':' + str(data_value) + '|' + self.create_data_string(data_set) + '\n')
            data_file.close()
            self.write_seek_count(seek_location, data_count)

    def read_seek_count(self, seek_location):
        self._seek.seek(seek_location * self._seek_byte_size)
        return int(str(self._seek.read(int(self._seek_byte_size)).rstrip('\x00')))

    def write_seek_count(self, seek_location, data_count):
        self._seek.seek(seek_location * self._seek_byte_size)
        self._seek.write(str(data_count + 1))

    def get_seek_location(self, value):
        seek_location = 0
        seek_value = value[:self._seek_char_size]
        if value.isnumeric():
            seek_value = seek_value.zfill(self._seek_char_size)
            seek_int_value = 0
            for x in range(self._seek_char_size):
                if x < (self._seek_char_size - 1):
                    seek_int_value += 25 * (26 ** (self._seek_char_size - (1 + x)))
                else:
                    seek_int_value += 26
                if config.debug():
                    print(str(x) + ': ' + str(seek_int_value))
            for x in range(len(seek_value)):
                if x < (self._seek_char_size - 1):
                    seek_int_value += int(seek_value[x]) * (10 ** (self._seek_char_size - (1 + x)))
                else:
                    seek_int_value += int(seek_value[x])
                if config.debug():
                    print(str(x) + ': ' + str(seek_int_value))
            seek_location = seek_int_value
            if config.debug():
                print("Seek Location: " + seek_value + ' ' + str(seek_int_value))
        else:
            seek_char_value = 0
            for x in range(len(seek_value)):
                if x < (self._seek_char_size - 1):
                    seek_char_value += (ord(seek_value[x]) - 97) * (26 ** (self._seek_char_size - (1 + x)))
                else:
                    seek_char_value += (ord(seek_value[x]) - 97)
                if config.debug():
                    print(str(x) + ': ' + str(seek_char_value))
            seek_location = seek_char_value
            if config.debug():
                print("Seek Location: " + str(seek_location))
        return seek_location + self._header_byte_size

    def build_new_seek(self, file):
        import itertools
        import string
        byte_location = self._header_byte_size
        seek_ascii_list = itertools.product(string.ascii_lowercase, repeat=self._seek_char_size)
        for seek_ascii_item in seek_ascii_list:
            file.seek(byte_location)
            file.write('0')
            byte_location += self._seek_byte_size
        seek_numbers_list = itertools.product('0123456789', repeat=self._seek_char_size)
        print(byte_location)
        for seek_number_item in seek_numbers_list:
            file.seek(byte_location)
            file.write('0')
            byte_location += self._seek_byte_size
        print(byte_location)
