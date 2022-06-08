from .Invalid import Invalid
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
            if self.state[pos] == '.':
                precision = 0
                pos += 1
                while (pos != self.tam and self.state[pos] in digits):
                    precision = precision * 10 + (int(self.state[pos]))
                    pos += 1

                self.stop_pos = pos
                v = float(f"{v}.{precision}")
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
                return Invalid(self.state[pos:self.stop_pos])


        if self.stop_pos != self.tam and self.state[pos] == '[':
            return LB()

        if self.stop_pos != self.tam and self.state[pos] == ']':
            return RB()

        if self.stop_pos != self.tam and self.state[pos] == '(':
            return LP()

        if self.stop_pos != self.tam and self.state[pos] == ')':
            return RP()

        if self.stop_pos != self.tam and self.state[pos] == '+':
            return Sum()

        if self.stop_pos != self.tam and self.state[pos] == '-':
            return Sub()

        if self.stop_pos != self.tam and self.state[pos] == '*':
            return Mul()

        if self.stop_pos != self.tam and self.state[pos] == '/':
            return Div()

        if self.stop_pos != self.tam and self.state[pos] == '^':
            return Pow()

        # Neither of types
        t = Invalid('')

        return t
