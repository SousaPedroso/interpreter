from .Token import Token
from .Tag import Tag

class Pow(Token):

    def __init__(self):
        super().__init__(Tag.POW)
        self.value = '^'