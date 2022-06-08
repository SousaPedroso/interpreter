from .Token import Token
from .Tag import Tag

class RB(Token):

    def __init__(self):
        super().__init__(Tag.RB)
        self.value = ']'