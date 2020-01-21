from vortex.nlp.word import Word


class Sentence:

    def __init__(self, _value):
        self._value = _value
        self._words = []
        split_words = str.split(_value, ' ')
        self.word_count = len(split_words)
        for split_words_keyword, split_words_value in enumerate(split_words):
            self._words.append(Word(split_words_value))

    def get_value(self):
        return self._value

    def get_word_count(self):
        return self.word_count

    def understand(self):
        for word in self._words:
            word.get_definition()

    def show_understanding(self):
        understanding = 0.0
        per_word_understanding = 100.0 / len(self._words)
        for word in self._words:
            if word.identified():
                understanding += per_word_understanding
        print(understanding, '% understood')