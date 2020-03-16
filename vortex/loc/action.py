class Action:

    def __init__(self, _word, _action):
        self._word = _word
        self._action = _action

    def get_word(self):
        return self._word

    def get_action(self):
        return self._action

    def key(self):
        return 'action'

    def value(self):
        return self._action
