from .Token import Token
from .Tag import Tag

class Float(Token):

    def __init__(self, v):
        super().__init__(Tag.FLOAT)
        self.value = v