Graph = {'A':[('B', 29), ('F', 10)],
        
        'B':[('A', 29), ('C', 16), ('G', 15)],

        'C':[('B', 16), ('D', 12)],

        'D':[('C', 12), ('E', 22), ('G', 18)],

        'E':[('D', 22), ('F', 27), ('G', 25)],

        'F':[('A', 10), ('E', 27)],

        'G':[('B', 15), ('D', 18), ('E', 25)]}

vertices = [-1, -1, -1, -1, -1, -1, -1]
eList = []

def edgeSort():
    for v in Graph:
        for e in Graph[v]:
            if v < e[0]:
                eList.append([v, e[0], e[1]])
    eList.sort(key= lambda e : e[2], reverse=True)
    for i in range(len(eList)-1, -1, -1):
        print('[%c%c%d] ' % (eList[i][0], eList[i][1], eList[i][2]), end='')
    print(); print()


def find(vNum):
    while vertices[vNum] != -1:
        vNum = vertices[vNum]
    return vNum

def union(vNum1, vNum2):
    vertices[vNum2] = vNum1


def kruskal():
    eCnt = 0
    vCnt = len(Graph)
    edgeSort()

    while eCnt < vCnt-1:
        e = eList.pop()
        vNum1 = find(ord(e[0])-65)
        vNum2 = find(ord(e[1])-65)
        if vNum1 != vNum2:
            eCnt += 1
            print('%d. [%s%s %d]' % (eCnt, e[0], e[1], e[2]))
            union(vNum1, vNum2)


if __name__ == '__main__':
    kruskal()
