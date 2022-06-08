from .Token import Token
from .Tag import Tag

class Mul(Token):

    def __init__(self):
        super().__init__(Tag.MUL)
        self.value = '*'