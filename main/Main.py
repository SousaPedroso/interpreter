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
    while token.tag != Tag.INVALID:
        print(token.value)
        token = lexer.get_token()
        if last_line == lexer.line:
            inputs[-1].append(token)
            entradas[-1].append(token.value)

        else:
            # $
            inputs[-1].append(EOS())
            inputs.append([token])
            entradas.append([token.value])

        last_line = lexer.line

    # Remove invalid token
    del(inputs[-1][-1])
    # Add EOS
    inputs[-1].append(EOS())
    # Remove invalid token
    del(entradas[-1][-1])
    syntatic = Syntatic(inputs, alert=True)
    accepted_sentence = syntatic.evaluate_input()
    while accepted_sentence:
        accepted_sentence = syntatic.evaluate_input()
    
    print("All sentences are syntatically corrects")

if __name__ == "__main__":
    main()
