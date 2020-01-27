from ..nlp.sentence import Sentence
from ..nlp.operation import Operation
from ..core import config
import time


class Thought(Operation):

    def __init__(self, _value):
        self._complete = False
        if _value[-1:] == '.':
            self._value = _value[:-1]
        else:
            self._value = _value
        self.data_set = []
        self._sentences = []
        split_sentences = str.split(self._value, '.')
        for split_sentences_keyword, split_sentences_value in enumerate(split_sentences):
            self._sentences.append(Sentence(split_sentences_value))

        if config.debug:
            print('Thought created with ' + str(len(self._sentences)) + ' sentences.')

    def get_value(self):
        return self._value

    def generate_time_iteration(self):
        if config.iteration() == 'second':
            return round(time.time())
        if config.iteration() == 'minute':
            return round(time.time() / 60)
        elif config.iteration() == 'hour':
            return round(time.time() / 60 / 60)
        elif config.iteration() == 'day':
            return round(time.time() / 60 / 60 / 24)
        else:
            return 0

    def process(self):
        for sentence in self._sentences:
            if sentence.input_identified:
                input_data_set = {}
                for word in sentence.get_words():
                    input_data_set.update(word.get_data_set())
                input_data_set['time_entered'] = self.generate_time_iteration()
                self.data_set.append(dict(input_data_set))

            if sentence.output_identified:
                for word in sentence.get_words():
                    if not word.identified():
                        print('Data: ' + word.raw_value)

    def get_data_set(self):
        return self.data_set
