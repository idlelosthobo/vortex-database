import os
from vortex.core import config


class DataSeek:

    def __init__(self, _seek_file_location):
        self._seek_char_size = config.seek_character_size()
        self._seek_file_location = _seek_file_location
        self._header_byte_size = len(config.file_header())
        self._seek_ok = False
        if not os.path.isfile(_seek_file_location):
            try:
                open(_seek_file_location, 'x')
                new_seek_file = open(_seek_file_location, 'r+', encoding='utf-8')
                if config.check_file_header(new_seek_file, _seek_file_location):
                    self.build_new_seek(new_seek_file)
                    new_seek_file.close()
            except:
                print('Failed to create seek file')

        self._seek = open(_seek_file_location, 'r+', encoding='utf-8')

        if config.check_file_header(self._seek, self._seek_file_location):
            self._seek_ok = True

    def data_seek_ok(self):
        return self._seek_ok

    def get_seek_value(self, seek_location):
        self._seek.seek(seek_location + self._header_byte_size)
        return bool(int(self._seek.read(int(1))))

    def read_seek_count(self, seek_location):
        self._seek.seek(seek_location + self._header_byte_size)
        return int(self._seek.read(int(1)))

    def write_seek_count(self, seek_location):
        self._seek.seek(seek_location + self._header_byte_size)
        self._seek.write('1')

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
        return seek_location

    def build_new_seek(self, file):
        import itertools
        import string
        byte_location = len(config.file_header())
        seek_ascii_list = itertools.product(string.ascii_lowercase, repeat=self._seek_char_size)
        for seek_ascii_item in seek_ascii_list:
            file.seek(byte_location)
            file.write('0')
            byte_location += 1
        seek_numbers_list = itertools.product('0123456789', repeat=self._seek_char_size)
        print(byte_location)
        for seek_number_item in seek_numbers_list:
            file.seek(byte_location)
            file.write('0')
            byte_location += 1
        print(byte_location)
