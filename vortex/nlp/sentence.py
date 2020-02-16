from ..nlp.word import Word
from vortex.core.operation import Operation
from ..core import config


class Sentence(Operation):

    def __init__(self, _value):
        self.raw_value = _value
        self.clean_value = self.clean(_value)
        self.word_count = 0
        self._words = []
        split_words = str.split(self.clean_value, ' ')
        word_position = 1
        for split_words_keyword, split_words_value in enumerate(split_words):
            self._words.append(Word(split_words_value, word_position))
            word_position += 1
        self.word_count = word_position - 1

    def get_value(self):
        return self.raw_value

    def get_words(self):
        return self._words

    def get_word_count(self):
        return self.word_count

    def clean(self, value):
        clean_value = value.replace(',', '')
        clean_value = clean_value.replace('"', '')
        clean_value = clean_value.strip()
        return clean_value

