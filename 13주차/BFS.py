Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import Queue

def BFS(u):
    Q = Queue()
    visited = [False] * len(Vertex)

    Q.put(u)
    print(Vertex[u], end=' ')
    visited[u] = True

    while not Q.empty():
        u = Q.get()
        for v in AdjVer[u]:
            if visited[v] == False:
                Q.put(v)
                print(Vertex[v], end=' ')
                visited[v] = True


if __name__ == '__main__':
    print('BFS(E) : ', end="")
    BFS(4)
    print()














