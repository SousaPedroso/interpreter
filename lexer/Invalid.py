from .Token import Token
from .Tag import Tag

class Invalid(Token):
    def __init__(self, v):
        super().__init__(Tag.INVALID)
        self.value = v