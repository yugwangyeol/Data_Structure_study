from ArrayStack import ArrayStack

map = [
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']
]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    
    return False

def DFS():
    print("DFS: ")
    s = ArrayStack(100)
    s.push((1, 0))
    while not s.isEmpty():
        pos = s.pop()
        print(pos, end='->')
        r, c = pos
        if map[r][c] == 'x':
            return True
        else:
            map[r][c] = '.'
            if isValidPos(r-1, c): s.push((r-1, c))
            if isValidPos(r+1, c): s.push((r+1, c))
            if isValidPos(r, c-1): s.push((r, c-1))
            if isValidPos(r, c+1): s.push((r, c+1))
        s.display()
    
    return False 

if __name__ == '__main__':
    result = DFS()
    if result:
        print("Success")
    else:
        print("Failed")