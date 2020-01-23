from ..nlp.operation import Operation
from ..locale.find import find_word

class Word(Operation):

    def __init__(self, _value):
        self._value = _value
        self.lower_value = _value.lower()
        self._identified = False
        if self.lower_value[-2:] != 'ss' and self.lower_value[-1:] == 's':
            self._plural = True
        else:
            self._plural = False


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

    def identified(self):
        return self._identified

    def get_value(self):
        return self._value
