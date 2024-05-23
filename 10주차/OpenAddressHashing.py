M = 13
table = [0]*M

def hashFn(key):
    return key % M

def hasfn2(key):
    return 11 - (key%11)

def getLinear(v,i):
    return (v+i) % M

def getQuadratic(v,i):
    return (v+i*i) % M

def getDouble(v,i,key):
    return (v+i*hasfn2(key)) % M

def insert(key):
    v = hashFn(key)
    i = 0

    while i < M:
        b = getLinear(v,i)
        #b = getQuadratic(v,i)
        #b = getDouble(v,i,key)
        if table[b] == 0 or table[b] == -1:
            table[b] = key
            return
        else:
            i += 1

def search(key):
    v = hashFn(key)
    i = 0

    while i < M:
        b = getLinear(v,i)
        #b = getQuadratic(v,i)
        #b = getDouble(v,i,key)

        print('[%d]'%table[b],end=' ')

        if table[b] == 0:
            return 0
        elif table[b] == key:
            return table[b]
        else:
            i += 1
    
    return 0

def delete(key):
    v = hashFn(key)
    i = 0

    while i < M:
        b = getLinear(v,i)
        #b = getQuadratic(v,i)
        #b = getDouble(v,i,key)

        print('[%d]'%table[b],end=' ')

        if table[b] == 0:
            print('No key to delete')
            return
        elif table[b] == key:
            table[b] = -1
            return 
        else:
            i += 1
    
    return 0

def display():
    print()
    print('Bucket    Key')
    print('----------------')
    for i in range(M):
        print('%2d %5d'%(i,table[i]))

if __name__ == '__main__':
    data = [45,27,88,9,71,60,46,38,24]
    for d in data:
        print('h(%d)=%d'%(d,hashFn(d)),end=' ')
        insert(d)
        print(table)
    display()

    print()

    delete(60)
    display()
    print('Search(60) ---->',search(60))
    print()
    print('Search(46) ---->',search(46))
    #print('Search(7) ---->',search(8))