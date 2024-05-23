from CircularQueue import CirclularQueue

map = [
    ['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']
]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    
    return False

def BFS():
    q = CirclularQueue(50)
    q.enqueue((1, 0))
    print("BFS: ")
    while not q.isEmpty():
        pos = q.dequeue()
        print(pos, end='->')
        r, c = pos
        if map[r][c] == 'x':
            return True
        else:
            map[r][c] = '.'
            if isValidPos(r-1, c): q.enqueue((r-1, c))
            if isValidPos(r+1, c): q.enqueue((r+1, c))
            if isValidPos(r, c-1): q.enqueue((r, c-1))
            if isValidPos(r, c+1): q.enqueue((r, c+1))
        q.display2()
    
    return False

if __name__ == '__main__':
    result = BFS()
    if result:
        print("Success")
    else:
        print("Failed")