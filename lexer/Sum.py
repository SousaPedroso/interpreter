from .Token import Token
from .Tag import Tag

class Sum(Token):

    def __init__(self):
        super().__init__(Tag.SUM)
        self.value = '+'