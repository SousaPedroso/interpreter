import os
from lexer.Lexer import Lexer
from lexer.Tag import Tag

def main():
    tests_dir = os.path.abspath("..\\tests")

    lexer = Lexer(os.path.join(tests_dir, "tokens"))
    token = lexer.get_token()
    while token.tag != Tag.INVALID:
        print(token.value)
            
        token = lexer.get_token()

if __name__ == "__main__":
    main()
