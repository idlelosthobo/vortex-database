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

    def thought_to_ideas(self, thought_obj):
        thought = thought_obj
        ideas = list()
        for sentence in thought.get_sentences():
            new_idea = Idea()
            stripped_sentence = ''
            # print('"' + sentence.get_value() + '"')
            for word in sentence.get_words():
                if word.is_number():
                    new_idea.add_data('number', word.trigger_value())
                    # print(word.raw_value() + ' is a Number')
                elif word.trigger_value() in self.all_words:
                    # print(word.raw_value() + ' identified')
                    stripped_sentence += word.trigger_value() + ' '
                else:
                    # print(word.raw_value() + ' not identified')
                    new_idea.add_data('object', word.trigger_value())
            if len(stripped_sentence) > 0:
                intention_found = False
                action_found = False
                quantify_found = False
                for intention in self._language.intentions:
                    if self.compare_statement(stripped_sentence, intention.sentence_segment()):
                        new_idea.evaluate_action(intention.database_action())
                        intention_found = True
                for action in self._language.actions:
                    if self.compare_statement(stripped_sentence, action.get_word()):
                        new_idea.add_data(action.key(), action.value())
                        action_found = True
                if not action_found:
                    for quantify in self._language.quantifies:
                        if self.compare_statement(stripped_sentence, quantify.get_word()):
                            new_idea.add_data(quantify.type(), quantify.value())
                            quantify_found = True
            print('Idea Database Action: ' + str(new_idea.get_database_action()))
            ideas.append(new_idea)
        return ideas

    def get_intention(self, stripped_sentence):
        pass

    def compare_statement(self, stripped_sentence, sentence_segment):
        match = False
        if stripped_sentence.strip() == sentence_segment:
            match = True
        else:
            words = stripped_sentence.strip().split(' ')
            word_count = len(words)
            word_iter_str = ''
            for x in range(word_count):
                word_iter_str += str(x)
            # print(word_iter_str)
            # print(word_count)
            # # print('"' + stripped_sentence + '"')
            for y in range(word_count):
                word_combinations = itertools.combinations(word_iter_str, y + 1)
                # print(list(word_combinations))
                for combination in word_combinations:
                    sentence_segment_combination = ''
                    # print(combination)
                    for z in range(len(combination)):
                        sentence_segment_combination += words[int(combination[z])] + ' '
                    # print(sentence_segment_combination.strip())
                    if sentence_segment_combination.strip() == sentence_segment:
                        match = True
        # print(sentence_segment + ' Match: ' + str(match))
        return match

    def advanced_compare_statement(self, stripped_sentence, sentence_segment):
        # This would compare iterated versions in both directions and make a assumption on intention
        pass

    def get_word_value(self, word):
        if word in self.all_words:
            return True

    def print_words(self):
        print('Words...')
        print(self.all_words)
