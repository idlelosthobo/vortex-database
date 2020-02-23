from importlib import import_module
from ..settings import APP_NAME, LANGUAGE
from vortex.nlp.idea import Idea
import itertools


class Locale:

    def __init__(self):
        self.all_words = set()
        self.intention_words = set()
        self.action_words = set()
        self.quantify_words = set()
        self._language = import_module(APP_NAME + '.loc.language.' + LANGUAGE + '')

        for intention in self._language.intentions:
            words = intention.get_words()
            for word in words:
                self.all_words.add(word)
                self.intention_words.add(word)

        for action in self._language.actions:
            self.all_words.add(action.get_word())
            self.action_words.add(action.get_word())

        for quantify in self._language.quantifies:
            self.all_words.add(quantify.get_word())
            self.quantify_words.add(quantify.get_word())

    def process_thought(self, thought_obj):
        thought = thought_obj
        ideas = list()
        for sentence in thought.get_sentences():
            new_idea = Idea
            stripped_sentence = ''
            # print('"' + sentence.get_value() + '"')
            for word in sentence.get_words():
                if word.is_number():
                    new_idea.add_data('number', word.trigger_value())
                    print(word.raw_value() + ' is a Number')
                elif word.trigger_value() in self.all_words:
                    print(word.raw_value() + ' identified')
                    stripped_sentence += word.trigger_value() + ' '
                else:
                    print(word.raw_value() + ' not identified')
                    new_idea.add_data('object', word.trigger_value())

        return thought

    def get_intention(self, stripped_sentence):
        pass

    def compare_statement(self, stripped_sentence, segment):
        words = stripped_sentence.split(' ')
        word_count = len(words)

    def get_word_value(self, word):
        if word in self.all_words:
            return True

    def print_words(self):
        print('Words...')
        print(self.all_words)
