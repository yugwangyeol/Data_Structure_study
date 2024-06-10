Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
        [0, 3],
        [0, 3, 4],
        [1, 2, 5],
        [2, 6, 7],
        [3],
        [4, 7],
        [4, 6]]

from queue import LifoQueue
visited = [False]*len(Vertex)

def iDFS(u):
    s = LifoQueue()
    s.put(u)

    while not s.empty():
        u = s.get()
        s.put(u)

        if visited[u] == False:
            visited[u] = True
            print(' %s ' % Vertex[u], end='')
        
        flag = True

        for v in AdjVer[u]:
            if visited[v] == False:
                s.put(v)
                flag = False
                break
        
        if flag == True:
            s.get()

if __name__ == '__main__':
    print(' iDFS(A) ', end='')
    iDFS(0)