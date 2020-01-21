class Definition:

    def __init__(self, _words, _type, _action, _direction, _intention, **kwargs):
        self._words = []
        split_words = str.split(_words, ' ')
        for split_words_keyword, split_words_value in enumerate(split_words):
            self._words.append(split_words_value)

        self._type = _type
        self._action = _action
        self._direction = _direction
        self._intention = _intention
        self.accepted_kwargs = ['context']
        for keyword, value in kwargs.items():
            if keyword in self.accepted_kwargs:
                setattr(self, '_'+keyword, value)
            else:
                raise ValueError('Unknown keyword argument: {!r}'.format(keyword))

    def compare_word(self, input_string, required_accuracy):
        for word in self._words:
            accuracy = 0
            if len(input_string) == len(word):
                if input_string == word:
                    accuracy = 100
                else:
                    match_value = 100 / len(word)
                    for i in range(len(word)):
                        if input_string[i] == word[i]:
                            accuracy += match_value
            if accuracy >= required_accuracy:
                return True

    def get_type(self):
        return self._type

    def get_intention(self):
        return self._intention

