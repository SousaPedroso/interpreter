import os
from lexer.Lexer import Lexer
from lexer.Tag import Tag
from lexer.EOS import EOS
from syntatic.Syntatic import Syntatic

def main():
    tests_dir = os.path.abspath("..\\tests")

    lexer = Lexer(os.path.join(tests_dir, "operations"))
    token = lexer.get_token()
    inputs = [[token]]
    last_line = lexer.line
    # Recover the values
    entradas = [[token.value]]
    while token.tag != Tag.EOS:
        # print(token.value)
        token = lexer.get_token()
        if last_line == lexer.line:
            inputs[-1].append(token)
            entradas[-1].append(token.value)

        else:
            # $
            inputs[-1].append(EOS())
            inputs.append([token])

        last_line = lexer.line

    syntatic = Syntatic(inputs, alert=False)
    accepted_sentence = syntatic.evaluate_input()
    while accepted_sentence:
        accepted_sentence = syntatic.evaluate_input()
    
    print("All sentences are syntatically corrects")

if __name__ == "__main__":
    main()
