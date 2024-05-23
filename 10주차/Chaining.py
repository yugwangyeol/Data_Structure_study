class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

M = 13

class HashTable:
    def __init__(self):
        self.table = [None]*M

    def hashFn(self,key):
        return key % M
    
    def insert(self,key):
        b = self.hashFn(key)
        node = Node(key)
        node.next = self.table[b]
        self.table[b] = node

    def display(self):
        for i in range(M):
            print('HT[%02d] : '%i,end='')
            n = self.table[i]
            if n == None:
                print()
            else:
                while n is not None:
                    print('[%d]'%n.data,end=' ')
                    n = n.next
                print()

if __name__ == "__main__":
    import random

    HT = HashTable()

    for _ in range(20):
        HT.insert(random.randint(10,99))
    
    HT.display()
