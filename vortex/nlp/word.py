from vortex.core.operation import Operation
from ..core import config


class Word(Operation):

    def __init__(self, _value, _position):
        if config.debug:
            Operation.__init__(self)
        self._raw_value = _value
        self._position = _position
        self._lower_value = _value.lower()
        self._trigger_value = _value.lower()
        self._plural = False
        self._number = False

        if len(self._lower_value) > 2 and self._lower_value[-2:] != 'ss' and self._lower_value[-1:] == 's':
            self._plural = True
            self._trigger_value = _value[:-1].lower()

        if self._trigger_value.isnumeric():
            self._number = True

    def trigger_value(self):
        return self._trigger_value

    def raw_value(self):
        return self._raw_value

    def is_number(self):
        return self._number

    def is_plural(self):
        return self._plural
