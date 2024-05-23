from CircularQueue import CirclularQueue

class CircularDeque(CirclularQueue):
    def __init__(self,capacity= 10):
        super().__init__(capacity)
    
    def addRear(self, e):
        self.enqueue(e)
    
    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass
    
    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear];
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            pass
    
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            pass

if __name__ == "__main__":
    import random
    dq = CircularDeque()

    for i in range(4):
        dq.addFront(random.randint(1,100))
    dq.display()

    for i in range(4):
        dq.addRear(random.randint(1,100))
    dq.display()

    for i in range(2):
        dq.deleteFront()
    dq.display()

    for i in range(2):
        dq.deleteRear()
    dq.display()