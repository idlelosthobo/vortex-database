class DataItem:

    def __init__(self, _key, _value):
        self._key = str(_key)
        self._value = str(_value)

    def key(self):
        return self._key

    def value(self):
        return self._value
