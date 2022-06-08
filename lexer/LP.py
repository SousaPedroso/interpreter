from .Token import Token
from .Tag import Tag

class LP(Token):

    def __init__(self):
        super().__init__(Tag.LP)
        self.value = '('