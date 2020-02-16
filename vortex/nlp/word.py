from vortex.core.operation import Operation
from ..core import config


class Word(Operation):

    def __init__(self, _value, _position):
        if config.debug:
            Operation.__init__(self)
        self.raw_value = _value
        self.position = _position
        self.lower_value = _value.lower()
        self.trigger_value = _value.lower()
        self._plural = False
        self._number = False
        self._data_set = {}

        if len(self.lower_value) > 2 and self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
            self.trigger_value = _value[:-1].lower()

        if self.trigger_value.isnumeric():
            self._number = True

    def get_trigger_value(self):
        return self.trigger_value

    def get_data_set(self):
        return self._data_set

    def plural(self):
        return self._plural

    def get_raw_value(self):
        return self.raw_value
