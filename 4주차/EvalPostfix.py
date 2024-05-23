from ArrayStack import ArrayStack


def evalPostfix(expr):
    S = ArrayStack(100)

    for token in expr:
        if token in '+-*/':
            op2 = S.pop()
            op1 = S.pop()
            if token == '+':
                S.push(op1 + op2)
            elif token == '-':
                S.push(op1 - op2)
            elif token == '*':
                S.push(op1 * op2)
            elif token == '/':
                S.push(op1 / op2)
        else:
            S.push(float(token))
    
    return S.pop()

if __name__ == '__main__':

    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()
    print(str, '----->', evalPostfix(expr))