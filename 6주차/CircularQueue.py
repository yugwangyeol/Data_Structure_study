class CirclularQueue:
    def __init__(self,capacity=8):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = 0 
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear+1) % self.capacity
            self.queue[self.rear] = e
        else:
            print("Overflow")
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.capacity
            return self.queue[self.front]
        else:
            print("Underflow")
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front+1) % self.capacity]
        else:
            print("Underflow")
    
    def display(self):
        print("Front : %d, Rear : %d"%(self.front,self.rear))
        i = self.front
        while i != self.rear:
            i = (i+1) % self.capacity
            print("[%c]"%self.queue[i],end=" ")
        print()
    
    def display2(self):
        print(self.queue[self.front+1:self.rear+1])
        
if __name__ == "__main__":
    q = CirclularQueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    q.display()
    print()

    print("Dequeue : %c"%q.dequeue())
    print("Dequeue : %c"%q.dequeue())
    print("Dequeue : %c"%q.dequeue())
    q.display()
    print()

    q.enqueue("F")
    q.enqueue("G")
    q.enqueue("H")
    q.enqueue("I")
    q.display()