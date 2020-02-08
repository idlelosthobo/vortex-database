from ..nlp.operation import Operation
from ..settings import APP_NAME, LOCALE
from importlib import import_module
from ..core import config

locale_words = import_module(APP_NAME + '.locale.' + LOCALE + '.words')
locale_quantify = import_module(APP_NAME + '.locale.' + LOCALE + '.quantify')
locale_actions = import_module(APP_NAME + '.locale.' + LOCALE + '.actions')


class Word(Operation):

    def __init__(self, _value, _position):
        if config.debug:
            Operation.__init__(self)
        self.raw_value = _value
        self.position = _position
        self.lower_value = _value.lower()
        self.trigger_value = _value.lower()
        self._quantified = False
        self.quantified_value = None
        self.quantified_unit = None
        self._identified = False
        self._action = False
        self._plural = False
        self._number = False
        self._accuracy = 0
        self._type = None
        self._data_set = {}

        if len(self.lower_value) > 2 and self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
            self.trigger_value = _value[:-1].lower()

        if self.trigger_value.isnumeric():
            self._number = True
            self._data_set['number'] = self.trigger_value
        elif self.trigger_value in locale_words.BASIC_WORDS:
            self._identified = True
        elif self.trigger_value in locale_actions.BASIC_ACTIONS:
            self._action = True
            self._data_set['action'] = self.trigger_value
        else:
            if self.trigger_value in locale_quantify.BASIC_QUANTIFY:
                split_quantify = str.split(locale_quantify.BASIC_QUANTIFY[self.trigger_value], ' ')
                self._quantified = True
                self.quantified_value = split_quantify[0]
                self.quantified_unit = split_quantify[1]
                self._data_set['value'] = split_quantify[0]
                self._data_set['unit'] = split_quantify[1]
            else:
                self._data_set['object'] = self.trigger_value

        if config.debug:
            debug = 'Word "' + self.raw_value + '" Identification: ' + str(self._identified)
            debug += ", Quantified: " + str(self.quantified_value) + ' ' + str(self.quantified_unit)
            # print('Word Process Time: ' + str(self.get_time_alive()))
            print(debug)

    def get_trigger_value(self):
        return self.trigger_value

    def get_data_set(self):
        return self._data_set

    def identified(self):
        return self._identified

    def quantified(self):
        return self._quantified

    def plural(self):
        return self._plural

    def get_raw_value(self):
        return self.raw_value
