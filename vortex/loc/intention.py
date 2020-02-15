class Intention:

    def __init__(self, _sentence_segment, _database_action):
        self._sentence_segment = _sentence_segment
        if _database_action == 'store' or 'retrieve':
            self._database_action = _database_action

    def get_words(self):
        words = self._sentence_segment.split(' ')
        return words

