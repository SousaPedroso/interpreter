<h1 align="center">Interpreter of arithmetic operations</h1>

This repository contains the final project os Compiler I subject at UFMT proposed by the professor <a href="https://github.com/thesivis">Raphael</a>.

The valid tokens of the language can be seen according to the following automata.

<p align="center">
  <img alt="Automata of the language" src="https://github.com/SousaPedroso/interpreter/blob/main/lexer/Lexer_Automata.png">
</p>

Using the ascendent syntatic, the automata which describes the rules for the <a href="https://github.com/SousaPedroso/interpreter/blob/main/language">language </a> is demonstrated below, using a dictionary in python:

<p align="center">
  <img alt="Automata of the rules" src="https://github.com/SousaPedroso/interpreter/blob/main/syntatic/Syntatic_Automata.svg">
</p>

None package was used for this project, but for execute it you must install this repository as a package due to the directories organization, running the following command on the root of this repository:

```
python -m pip install -e .
```

You can execute the <a href="https://github.com/SousaPedroso/interpreter/blob/main/main/Main.py">main program</a> passing the `alert` argument to $true$ or $false$
execute the sentences in <a href="https://github.com/SousaPedroso/interpreter/blob/main/tests/operations">operations file</a> showing or not the reductions for each sentence. Also, you can add more operations for each line of the line if you would like to see more operations.
