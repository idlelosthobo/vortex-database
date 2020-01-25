from ..nlp.operation import Operation
from ..settings import PACKAGE_NAME, LOCALE
from importlib import import_module

locale_input = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.input')
locale_output = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.output')
locale_words = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.words')


class Word(Operation):

    def __init__(self, _value):
        self._value = _value
        self.lower_value = _value.lower()
        self._identified = False
        self._accuracy = 0
        self._type = None
        if self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
            self.lower_value = _value[:-1].lower()
        else:
            self._plural = False
            self.lower_value = _value.lower()

    def compare_word(self):
        pass

    def identified(self):
        return self._identified

    def get_value(self):
        return self._value
