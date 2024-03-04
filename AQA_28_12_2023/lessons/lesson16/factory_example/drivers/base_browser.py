from abc import ABC


class Browser(ABC):
    _name = ''

    def __init__(self):
        self.history = []