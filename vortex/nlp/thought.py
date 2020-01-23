from ..nlp.sentence import Sentence
from ..nlp.operation import Operation
from ..core import config


class Thought(Operation):

    def __init__(self, _value):
        self._complete = False
        self._value = _value

        self._sentences = []
        split_sentences = str.split(self._value, '.')
        for split_sentences_keyword, split_sentences_value in enumerate(split_sentences):
            self._sentences.append(Sentence(split_sentences_value))

        if config.debug:
            print('Thought created with ' + str(len(self._sentences)) + ' sentences.')

    def get_value(self):
        return self._value


