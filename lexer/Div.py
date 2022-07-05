from .Token import Token
from .Tag import Tag

class Div(Token):

    def __init__(self):
        super().__init__(Tag.DIV)
        self.value = "/"