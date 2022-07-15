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
    {"T": {")": ["r", "T", 3], "^": ["s", 12], "*": ["r", "T", 3], "/": ["r", "T", 3], "+": ["r", "T", 3], "-": ["r", "T", 3], "$": ["r", "T", 3]}}, #I18
    {"T": {"]": ["s", 20]}}, #I19
    {"T": {")": ["r", "P", 4], "^": ["r", "P", 4], "*": ["r", "P", 4], "/": ["r", "P", 4], "+": ["r", "P", 4], "-": ["r", "P", 4], "$": ["r", "P", 4]}}, #I20
    {"T": {")": ["s", 22], "+": ["s", 8], "-": ["s", 9]}}, #I21
    {"T": {")": ["r", "F", 3], "]": ["r", "F", 3], "^": ["r", "F", 3], "*": ["r", "F", 3], "/": ["r", "F", 3], "+": ["r", "F", 3], "-": ["r", "F", 3], "$": ["r", "F", 3]}}] # I22

    # Types for each rule
    # I: Ihnerate (for symbol only, actually it is a synthetized attribute)
    # A: Add
    # S: Sub
    # M: Mult
    # D: Div
    # P: Power
    # E: exp
    # R: Reduce (remove the symbol from the stack 'E')

    # Defines how each non terminal will be updated according to the operation
    operations = {"I": lambda S: S, "A": lambda E, T:  E+T, "S": lambda E, T:  E-T,
    "M": lambda T, P: T*P, "D": lambda T, P: T/P, "P": lambda P, F: P**F, "E": lambda F: 2.71828**F,
    "R": lambda E: E.pop()}

    # Stores the rules to each state to recover the value for each operation
    rules = {
        2: {")": "I", "+": "I", "-": "I", "$": "I"},
        3: {")": "I", "*": "I", "/": "I", "+": "I", "-": "I", "$": "I"},
        5: {")": "I", "^": "I", "*": "I", "/": "I", "+": "I", "-": "I", "$": "I"},
        7: {")": "I", "]": "I", "^": "I", "*": "I", "/": "I", "+": "I", "-": "I", "$": "I"},
        14: {")": "A", "+": "A", "-": "A", "$": "A"},
        15: {")": "S", "+": "S", "-": "S", "$": "S"},
        16: {")": "P", "^": "P", "*": "P", "/": "P", "+": "P", "-": "P", "$": "P"},
        17: {")": "M", "*": "M", "/": "M", "+": "M", "-": "M", "$": "M"},
        18: {")": "D", "*": "D", "/": "D", "+": "D", "-": "D", "$": "D"},
        20: {")": "E", "^": "E", "*": "E", "/": "E", "+": "E", "-": "E", "$": "E"},
        22: {")": "R", "]": "R", "^": "R", "*": "R", "/": "R", "+": "R", "-": "R", "$": "R"}
    }

    def __init__(self, inputs, alert=False):
        self.alert = alert
        self.current = 0 # Current input
        self.inputs = inputs
        self.reset_state()
        # S indicates for which value the state must be updated
        # R has two values, 1 string for indicate which token will substitute the current(s) and
        # a integer indicating the number of tokens to remove

    def reset_state(self):
        # Stores the symbols and update the values for each operation
        # Remembering that "E" contains the final result
        # "id" is here just for facilitate the operations
        self.non_terminals = {"E": [], "T": [], "P": [], "F": [], "id": 0}
        self.states = [0]
        self.symbols = []
        self.action = "T" # Search on Terminals or NonTerminals
        self.accepted = False

        # Considerate the rule F-> (E), the value is overrided because
        # this rule is used the same way as E -> T

        # E -> T, probably must save this result and not just override (rule 3)
        # E must be a list, with a initial value, appending the values

        # Para cada terminal, pode haver recursão, Assim
        # Uma pilha deve ser salva para cada um, permitindo recuperar valores

    def evaluate_input(self):
        # Abbreviation
        inputs = self.inputs

        # Print the current input
        if self.current < len(inputs) and self.alert:
            print(f"Input {self.current+1}")

        for inp in range(self.current, len(self.inputs)):

            while not(self.accepted):
                # Int or Float must be checked as id
                if inputs[inp][0].tag == Tag.INT or inputs[inp][0].tag == Tag.FLOAT:
                    value = "id"
                    # Store the value for the terminal symbol
                    self.non_terminals["id"] = inputs[inp][0].value
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
                            last_input = self.inputs[inp][0]
                            del(self.inputs[inp][0])

                        # reduce
                        elif action[0] != 'acc':

                            if self.alert:
                                print("Reduced ", end="")

                            # Get the rule for the value
                            rule = self.rules.get(self.states[-1])
                            rule_type = rule.get(value)

                            # Store the symbol position to print it
                            symbol = len(self.symbols)-action[2]

                            # print(rule_type, self.non_terminals)
                            if rule_type == "I":
                                # Push the value
                                # Can be removed from other stack (if not id)
                                if self.symbols[-1] != "id":
                                    self.non_terminals[action[1]].append(self.non_terminals[self.symbols[-1]][-1])
                                    self.operations.get("R")(self.non_terminals[self.symbols[-1]])

                                else:
                                    self.non_terminals[action[1]].append(self.non_terminals[self.symbols[-1]])


                            # F -> (E)
                            elif rule_type == "R":
                                self.non_terminals["F"].append(self.non_terminals["E"][-1])
                                self.operations.get("R")(self.non_terminals["E"])

                            # other operations except exp
                            elif action[2] == 3:
                                # Make the operation considering the values for both symbols
                                self.non_terminals[action[1]][-1] = self.operations.get(rule_type)(
                                    self.non_terminals[self.symbols[symbol]][-1], self.non_terminals[self.symbols[-1]][-1])

                            # exp operation
                            else:
                                # Pass the value of non terminal
                                non_terminal = self.non_terminals[self.symbols[symbol+2]][-1]
                                self.non_terminals[action[1]][-1] = self.operations.get("E")(non_terminal)

                            # Remove symbols
                            for _ in range(action[2]):
                                if self.alert:
                                    print(self.symbols[symbol], end="")
                                del(self.symbols[symbol])
                                del(self.states[-1])

                            # Update the last 
                            # Add the correspondent symbol
                            self.symbols.append(action[1])
                            # Check for next Nonterminal
                            self.action = 'N'
                            if self.alert:
                                print(f" to {action[1]}")

                        # accepted sentence
                        else:
                            # First value of the stack (and probably the only one)
                            print(f"Value for the input {self.current+1}: {str(self.non_terminals['E'][0]).replace('.', ',')}")
                            self.accepted = True
                            self.current += 1
                            self.reset_state()
                            return True

                    # Syntax error
                    else:
                        # Need more values
                        if value != "$":
                            raise SyntaxError(f"Unexpected {value} after {last_input.value}")

                        else:
                            raise SyntaxError(f"It was expected a sentence or value after {last_input.value}")
                    
                # Update state
                else:
                    action = self.table[self.states[-1]]
                    self.states.append(action.get("N").get(self.symbols[-1]))
                    self.action = 'T'
                    if self.alert:
                        print(f"Deviation for state {self.states[-1]}")

        return False