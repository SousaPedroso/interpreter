from .Token import Token
from .Tag import Tag

class LB(Token):

    def __init__(self):
        super().__init__(Tag.LB)
        self.value = "["