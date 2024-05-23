from ArrayStack import ArrayStack

def checkBrackets(str):
    s = ArrayStack(100)

    for c in str:
        if c == '[' or c == '(' or c == '{':
            s.push(c)
        elif c == ']' or c == ')' or c == '}':
            if s.isEmpty():
                return False
            else:
                left = s.pop()
                if (c == ']' and left != '[') or \
                    (c == ')' and left != '(') or \
                    (c == '}' and left != '{'):
                    return False
    
    return s.isEmpty()

if __name__ == '__main__':
    s1 = "{ A[(i+1)] = 0; }"
    s2 = "{ A[(i+1]) = 0; }"

    print(s1, '----->', checkBrackets(s1))
    print(s2, '----->', checkBrackets(s2))

    filename = './test.txt'
    inFile = open(filename, 'r')
    str = inFile.read()
    inFile.close()

    print(filename, '----->', checkBrackets(str))