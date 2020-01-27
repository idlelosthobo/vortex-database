from ..nlp.word import Word
from ..nlp.operation import Operation
from ..core import config
from ..settings import APP_NAME, LOCALE
from importlib import import_module

locale_input = import_module(APP_NAME + '.locale.' + LOCALE + '.input')
locale_output = import_module(APP_NAME + '.locale.' + LOCALE + '.output')


class Sentence(Operation):

    def __init__(self, _value):
        self.raw_value = _value
        self.clean_value = self.clean(_value)
        self.trigger_value = ''
        self.input_identified = False
        self.output_identified = False
        self._words = []
        split_words = str.split(self.clean_value, ' ')
        for split_words_keyword, split_words_value in enumerate(split_words):
            self._words.append(Word(split_words_value))
        for word in self._words:
            if word.identified() is True:
                self.trigger_value += word.trigger_value + ' '
        self.trigger_value = self.trigger_value[:-1]
        if self.trigger_value in locale_input.BASIC_INPUT:
            self.input_identified = True
        if self.trigger_value in locale_output.BASIC_OUTPUT:
            self.output_identified = True
        if config.debug():
            print('Trigger Value "' + self.trigger_value + '"')
            print('Input Trigger Identified: ' + str(self.input_identified))
            print('Output Trigger Identified: ' + str(self.output_identified))

    def get_value(self):
        return self.raw_value

    def get_words(self):
        return self._words

    def get_word_count(self):
        return len(self.words)

    def understand(self):
        for word in self._words:
            word.get_definition()

    def clean(self, value):
        clean_value = value.replace(',', '')
        clean_value = clean_value.replace('"', '')
        return clean_value

    def show_understanding(self):
        understanding = 0.0
        per_word_understanding = 100.0 / len(self._words)
        for word in self._words:
            if word.identified():
                understanding += per_word_understanding
        print('' + str(understanding) + '% understood')

