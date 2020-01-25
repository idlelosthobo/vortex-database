from ..nlp.operation import Operation
from ..settings import PACKAGE_NAME, LOCALE
from importlib import import_module
from ..core import config

locale_words = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.words')
locale_quantify = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.quantify')


class Word(Operation):

    def __init__(self, _value):
        if config.debug:
            Operation.__init__(self)
        self.raw_value = _value
        self.lower_value = _value.lower()
        self.trigger_value = _value.lower()
        self._quantified = False
        self.quantified_value = None
        self.quantified_unit = None
        self._plural = False
        self._accuracy = 0
        self._type = None

        if len(self.lower_value) > 2 and self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
            self.trigger_value = _value[:-1].lower()

        if self.lower_value in locale_words.BASIC_WORDS:
            self._identified = True
        else:
            self._identified = False
            if self.trigger_value in locale_quantify.BASIC_QUANTIFY:
                split_quantify = str.split(locale_quantify.BASIC_QUANTIFY[self.trigger_value], ' ')
                self.quantified_value = split_quantify[0]
                self.quantified_unit = split_quantify[1]

        if config.debug:
            debug = 'Word "' + self.raw_value + '" Identification: ' + str(self._identified)
            debug += ", Quantified: " + str(self.quantified_value) + ' ' + str(self.quantified_unit)
            # print('Word Process Time: ' + str(self.get_time_alive()))
            print(debug)

    def get_trigger_value(self):
        return self.trigger_value

    def identified(self):
        return self._identified

    def plural(self):
        return self._plural

    def get_raw_value(self):
        return self.raw_value
