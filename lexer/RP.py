from .Token import Token
from .Tag import Tag

class RP(Token):

    def __init__(self):
        super().__init__(Tag.RP)
        self.value = ')'