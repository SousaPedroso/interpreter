from .Token import Token
from .Tag import Tag

class Exp(Token):

    def __init__(self):
        super().__init__(Tag.EXP)
        self.value = 2.71828