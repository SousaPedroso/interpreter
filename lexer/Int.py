from .Token import Token
from .Tag import Tag

class Int(Token):

    def __init__(self, v):
        super().__init__(Tag.INT)
        self.value = v