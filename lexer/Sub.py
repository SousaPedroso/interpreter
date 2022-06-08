from .Token import Token
from .Tag import Tag

class Sub(Token):

    def __init__(self):
        super().__init__(Tag.SUB)