from vortex.object.data import Data
from vortex.object.sentence import Sentence
from drugen.logic.interpret import read_words


class Thought(Data):

    def __init__(self, _weight, _type, **kwargs):
        self._complete = False
        self._weight = _weight

        self.accepted_type = ['listen', 'speak']
        if _type in self.accepted_type:
            self._type = _type

        self.accepted_kwargs = ['sentence']
        for keyword, value in kwargs.items():
            if keyword in self.accepted_kwargs:
                if keyword == 'sentence':
                    self._sentences = []
                    split_sentences = str.split(value, '.')
                    for split_sentences_keyword, split_sentences_value in enumerate(split_sentences):
                        self._sentences.append(Sentence(split_sentences_value))
                else:
                    setattr(self, '_'+keyword, value)
            else:
                raise ValueError('Unknown keyword argument: {!r}'.format(keyword))

    def __str__(self):
        return 'Type: ' + self._type + ' Weight: ' + self._weight

    def get_weight(self):
        return self._weight

    def get_type(self):
        return self._type

    def process(self):
        print('Processing... ' + self._type)
        if self._type == 'listen':
            for sentence in self._sentences:
                print('Heard: ', sentence.get_value())
            print('I am going ot read these now.')
            sentence.understand()
            sentence.show_understanding()
            self._type = 'read'
        elif self._type == 'read':
            pass

    def set_complete(self):
        self._complete = True

    def is_complete(self):
        return self._complete