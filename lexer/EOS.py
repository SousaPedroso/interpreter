from .Token import Token
from .Tag import Tag

class EOS(Token):

    def __init__(self) -> None:
        super().__init__(Tag.EOS)
        self.value = "$"