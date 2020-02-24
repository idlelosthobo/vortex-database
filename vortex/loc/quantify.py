class Quantify:

    def __init__(self, _word, _value, _type):
        self._word = _word
        self._value = _value
        self._type = _type

    def get_word(self):
        return self._word

    def value(self):
        return self._value

    def type(self):
        return self._type
