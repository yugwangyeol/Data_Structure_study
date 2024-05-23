class ArrayList:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self,pos,e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size,pos,-1):
                self.array[i] == self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else:
            pass

    def delete(self,pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos,self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else: pass

    def findItem(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        return -1

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def replace(self,pos,e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        else: pass
    
    def gerEntry(self,pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: pass

if __name__ == "__main__":
    array_1 = ArrayList()
    array_1.insert(0,'A')
    array_1.insert(1,'B')
    array_1.insert(2,'C')
    array_1.insert(1,'D')

    array_1.display()

    e = input('Input item to delete : ')
    idx = array_1.findItem(e)
    if idx != -1:
        array_1.delete(idx)
        array_1.display()