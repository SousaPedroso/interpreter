from .InvalidTokenError import InvalidTokenError
from .Pow import Pow
from .Int import Int
from .Float import Float
from .Exp import Exp
from .Div import Div
from .LB import LB
from .LP import LP
from .Mul import Mul
from.RB import RB
from .RP import RP
from .Sub import Sub
from .Sum import Sum
from .EOS import EOS

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
exp = 'exp'

class Lexer:
    line = 1
    stop_pos = 0

    def __init__(self, f):
        with open(f, "r") as file:
            self.state = file.read()
            self.tam = len(self.state)

    def get_token(self):
        pos = 0
        for pos in range(self.stop_pos, self.tam):
            if self.state[pos] == '\t' or self.state[pos] == ' ':
                continue

            elif self.state[pos] == '\n':
                self.line += 1

            else:
                break

        # Check if it is digit
        if self.stop_pos != self.tam and self.state[pos] in digits:
            v = 0
            while (pos != self.tam and self.state[pos] in digits):
                v = v*10 + (int(self.state[pos]))

                pos += 1


            # Checks if Int or Float
            if pos != self.tam and self.state[pos] == ',':
                precision = 0
                pos += 1
                while (pos != self.tam and self.state[pos] in digits):
                    precision = precision * 10 + (int(self.state[pos]))
                    pos += 1

                self.stop_pos = pos
                v = f"{v},{precision}"
                return Float(v)

            else:
                self.stop_pos = pos
                return Int(v)

        # Check if it is the exp operation
        if self.stop_pos != self.tam and self.state[pos] in exp:
            buffer = ""
            exp_pos = 0
            while (pos != self.tam and exp_pos < 3 and self.state[pos+exp_pos] == exp[exp_pos]):
                buffer = f"{buffer}{self.state[pos]}"
                exp_pos += 1
            
            # If concluded, it is exp operation, else invalid token
            self.stop_pos = pos+exp_pos
            if exp_pos == 3:
                return Exp()

            else:
                raise InvalidTokenError(f"Invalid token {self.state[pos:pos+exp_pos+1]} at line {self.line}")


        if self.stop_pos != self.tam and self.state[pos] == '[':
            self.stop_pos = pos+1
            return LB()

        if self.stop_pos != self.tam and self.state[pos] == ']':
            self.stop_pos = pos+1
            return RB()

        if self.stop_pos != self.tam and self.state[pos] == '(':
            self.stop_pos = pos+1
            return LP()

        if self.stop_pos != self.tam and self.state[pos] == ')':
            self.stop_pos = pos+1
            return RP()

        if self.stop_pos != self.tam and self.state[pos] == '+':
            self.stop_pos = pos+1
            return Sum()

        if self.stop_pos != self.tam and self.state[pos] == '-':
            self.stop_pos = pos+1
            return Sub()

        if self.stop_pos != self.tam and self.state[pos] == '*':
            self.stop_pos = pos+1
            return Mul()

        if self.stop_pos != self.tam and self.state[pos] == '/':
            self.stop_pos = pos+1
            return Div()

        if self.stop_pos != self.tam and self.state[pos] == '^':
            self.stop_pos = pos+1
            return Pow()

        if self.stop_pos == self.tam:
            # Last token
            return EOS()

        # Invalid token
        else:
            raise InvalidTokenError(f"Invalid token {self.state[pos]} at line {self.line}")