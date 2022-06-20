from .SyntaxError import SyntaxError
from lexer.Tag import Tag

class Syntatic:
    accepted = False
    # T for terminal symbos and N for nonterminal symbols
    # s for shift and r for reduce. Reduce has one more element on the list
    # representing the token to substitue the current symbols. The last value 
    # is the number of symbols to remove before append the symbol
    # In shift and Nonterminals the number is for update the state
    table = [{"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"E": 1, "T": 2, "P": 3, "F": 5}}, # I0
    {"T": {"+": ["s", 8], "-": ["s", 9], "$": ["acc"]}}, # I1
    {"T": {")": ["r", "E", 1], "*": ["s", 10], "/": ["s", 11], "+": ["r", "E", 1], "-": ["r", "E", 1], "$": ["r", "E", 1]}}, # I2
    {"T": {")": ["r", "T", 1], "^": ["s", 12], "*": ["r", "T", 1], "/": ["r", "T", 1], "+": ["r", "T", 1], "-": ["r", "T", 1], "$": ["r", "T", 1]}}, # I3
    {"T": {"[": ["s", 13]}}, # I4
    {"T": {")": ["r", "P", 1], "^": ["r", "P", 1], "*": ["r", "P", 1], "/": ["r", "P", 1], "+": ["r", "P", 1], "-": ["r", "P", 1], "$": ["r", "P", 1]}}, # I5
    {"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"E": 21, "T": 2, "P": 3, "F": 5}}, # I6
    {"T": {")": ["r", "F", 1], "]": ["r", "F", 1], "^": ["r", "F", 1], "*": ["r", "F", 1], "/": ["r", "F", 1], "+": ["r", "F", 1], "-": ["r", "F", 1], "$": ["r", "F", 1]}}, # I7
    {"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"T": 14, "P": 3, "F": 5}}, # I8
    {"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"T": 15, "P": 3, "F": 5}}, # I9
    {"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"P": 17, "F": 5}}, # I10
    {"T": {"(": ["s", 6], "exp": ["s", 4], "id": ["s", 7]}, "N": {"P": 18, "F": 5}}, # I11
    {"T": {"(": ["s", 6], "id": ["s", 7]}, "N": {"F": 16}}, # I12
    {"T": {"(": ["s", 6], "id": ["s", 7]}, "N": {"F": 19}}, # I13
    {"T": {")": ["r", "E", 3], "*": ["s", 10], "/": ["s", 11], "+": ["r", "E", 3], "-": ["r", "E", 3], "$": ["r", "E", 3]}}, #I14
    {"T": {")": ["r", "E", 3], "*": ["s", 10], "/": ["s", 11], "+": ["r", "E", 3], "-": ["r", "E", 3], "$": ["r", "E", 3]}}, #I15
    {"T": {")": ["r", "P", 3], "^": ["r", "P", 3], "*": ["r", "P", 3], "/": ["r", "P", 3], "+": ["r", "P", 3], "-": ["r", "P", 3], "$": ["r", "P", 3]}}, #16
    {"T": {")": ["r", "T", 3], "^": ["s", 12], "*": ["r", "T", 3], "/": ["r", "T", 3], "+": ["r", "T", 3], "-": ["r", "T", 3], "$": ["r", "T", 3]}}, #I17
    {"T": {")": ["r", "T", 3], "*": ["r", "T", 3], "/": ["r", "T", 3], "+": ["r", "T", 3], "-": ["r", "T", 3], "$": ["r", "T", 3]}}, #I18
    {"T": {"]": ["s", 20]}}, #I19
    {"T": {")": ["r", "P", 4], "^": ["r", "P", 4], "*": ["r", "P", 4], "/": ["r", "P", 4], "+": ["r", "P", 4], "-": ["r", "P", 4], "$": ["r", "P", 4]}}, #I20
    {"T": {")": ["s", 22], "+": ["s", 8], "-": ["s", 9]}}, #I21
    {"T": {")": ["r", "F", 3], "]": ["r", "F", 3], "^": ["r", "F", 3], "*": ["r", "F", 3], "/": ["r", "F", 3], "+": ["r", "F", 3], "-": ["r", "F", 3], "$": ["r", "F", 3]}}] # I22

    def __init__(self, inputs, alert=False):
        self.alert = alert
        self.current = 0 # Current input
        self.inputs = inputs
        self.reset_state()

        # S indicates for which value the state must be updated
        # R has two values, 1 string for indicate which token will substitute the current(s) and
        # a integer indicating the number of tokens to remove

    def reset_state(self):
        self.states = [0]
        self.symbols = []
        self.action = "T" # Search on Terminals or NonTerminals
        self.accepted = False

    def evaluate_input(self):
        # Abbreviation
        inputs = self.inputs
        print(self.current)
        for inp in range(self.current, len(self.inputs)):

            while not(self.accepted):
                # print(self.states, self.inputs[inp])
                # Int or Float must be checked as id
                if inputs[inp][0].tag == Tag.INT or inputs[inp][0] == Tag.FLOAT:
                    value = "id"
                else:
                    if inputs[inp][0].tag != Tag.EXP:
                        value = inputs[inp][0].value
                    else:
                        value = "exp"

                # Action for terminals
                if self.action == "T":
                    # Check if it is ok
                    action = self.table[self.states[-1]].get("T").get(value)
                    if action != None:
                        # Push state and symbols
                        # Check shift
                        if action[0] != 'acc' and action[0] == 's':
                            if self.alert:
                                print(f"Shift to {action[1]}")

                            self.states.append(action[1])
                            self.symbols.append(value)
                            del(self.inputs[inp][0])

                        # reduce
                        elif action[0] != 'acc':
                            if self.alert:
                                print("Reduce ", end="")

                            # Remove symbols
                            for _ in range(action[2]):
                                if self.alert:
                                    print(self.symbols[-1], end=" ")
                                del(self.symbols[-1])
                                del(self.states[-1])

                            # Add the correspondent symbol
                            self.symbols.append(action[1])
                            # Check for next Nonterminal
                            self.action = 'N'
                            if self.alert:
                                print(f"to {action[1]}")

                        # accepted sentence
                        else:
                            self.accepted = True
                            self.current += 1
                            self.reset_state()
                            return True

                    # Syntax error
                    else:
                        raise SyntaxError(f"Unexpected {value} after {self.symbols[-1]}")
                    
                # Update state
                else:
                    action = self.table[self.states[-1]]
                    self.states.append(action.get("N").get(self.symbols[-1]))
                    self.action = 'T'
                    if self.alert:
                        print(f"Deviation for state {self.states[-1]}")

        return False