from EvalPostfix import evalPostfix
from InfixtoPostfix import infix_to_postfix

infix = input('Infix expression: ')
expr = infix.split()

print(infix, '----->', evalpostfix(infix_to_postfix(expr)))