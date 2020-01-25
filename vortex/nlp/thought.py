from ..nlp.sentence import Sentence
from ..nlp.operation import Operation
from ..core import config


class Thought(Operation):

    def __init__(self, _value):
        self._complete = False
        if _value[-1:] == '.':
            self._value = _value[:-1]
        else:
            self._value = _value
        self._sentences = []
        split_sentences = str.split(self._value, '.')
        for split_sentences_keyword, split_sentences_value in enumerate(split_sentences):
            self._sentences.append(Sentence(split_sentences_value))

        for sentence in self._sentences:
            if sentence.input_identified:
                for word in sentence.get_words():
                    if not word.identified():
                        print('Data: ' + word.raw_value)

            if sentence.output_identified:
                for word in sentence.get_words():
                    if not word.identified():
                        print('Data: ' + word.raw_value)

        if config.debug:
            print('Thought created with ' + str(len(self._sentences)) + ' sentences.')

    def get_value(self):
        return self._value
