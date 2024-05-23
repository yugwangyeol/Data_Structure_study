class ArraySet:
    
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def contains(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False
    
    def insert(self,e):
        if not self.isFull() and not self.contains(e):
            self.array[self.size] = e
            self.size += 1
        else: pass
    
    def delete(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]
                self.size -= 1
                return e
    
    def union(self,setB):
        setC = ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
        
        for i in range(setB.size):
            setC.insert(setB.array[i])
        
        return setC
    
    def intersection(self,setB):
        setC = ArraySet()
        
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        
        return setC
    
    def difference(self,setB):
        setC = ArraySet()
        
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        
        return setC
    
    def __eq__(self,setB):
        if self.size != setB.size:
            return False
        
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                return False
        
        return True

if __name__ == "__main__": 
    s = ArraySet()
    s.insert(10)
    s.insert(20)
    s.insert(30)
    s.insert(40)

    s.display()

    T = ArraySet()
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(10)
    T.display()

    s.union(T).display()
    s.intersection(T).display()
    s.difference(T).display()
    print(s == T)

    # 연산자 중복


