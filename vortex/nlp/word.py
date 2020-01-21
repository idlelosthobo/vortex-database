from vortex.loc.english_canada.common import common_words


class Word:

    def __init__(self, _value):
        self._value = _value
        self.lower_value = _value.lower()
        self._identified = False
        self._type = ''
        self._intention = ''
        if self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
        else:
            self._plural = False

    def get_definition(self):
        for definition in common_words:
            if definition.compare_word(self._value, 75):
                self._type = definition.get_type()
                self._intention = definition.get_intention()
                self._identified = True

    def identified(self):
        return self._identified

    def get_value(self):
        return self._value
