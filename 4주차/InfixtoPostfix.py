from ArrayStack import ArrayStack

def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def infixToPostfix(expr):
    S = ArrayStack(100)

    postfix = []

    for token in expr:
        if token in '(':
            S.push(token)
        elif token in ')':
            while not S.isEmpty():
                top = S.pop()
                if top == '(':
                    break
                postfix.append(top)
        elif token in '+-*/':
            while not S.isEmpty():
                top = S.peek()
                if precedence(token) <= precedence(top):
                    postfix.append(top)
                    S.pop()
                else:
                    break
            S.push(token)
        else:
            postfix.append(token)

    while not S.isEmpty():
        postfix.append(S.pop())

    return postfix

if __name__ == '__main__':
    str = '3+5/6*(24-1)'#input('Infix expression: ')
    expr = str.split()
    print(str, '----->', infixToPostfix(expr))

