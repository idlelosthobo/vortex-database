from importlib import import_module
from ..settings import APP_NAME, LANGUAGE
from ..nlp.thought import Thought


class Locale:

    def __init__(self):
        self._words = ()
        self._intentions = import_module(APP_NAME + '.loc.language.' + LANGUAGE + '.intentions')
        for intention in self._intentions:
            words = intention.get_words()
            for word in words:
                self._words += word
        print(self._words)

    def process_thought(self, thought):
        thought = thought

