from ..settings import PACKAGE_NAME, LOCALE
from importlib import import_module

input_stuff = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.input')
output_stuff = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.output')
words_stuff = import_module(PACKAGE_NAME + '.locale.' + LOCALE + '.words')


def find_word(value):
    print(input_stuff.BASIC_INPUT_TRIGGERS)