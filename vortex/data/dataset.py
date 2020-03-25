from vortex.data.dataitem import DataItem


class DataSet:

    def __init__(self):
        self._data_items = list()

    def add_data_item(self, key, value):
        self._data_items.append(DataItem(key, value))

    def get_data_items(self):
        return self._data_items

    def get_data_set_string(self):
        data_string = ''
        for data in self._data_items:
            data_string += str(data.key()) + ':' + str(data.value()) + ','
        return data_string[:-1]

