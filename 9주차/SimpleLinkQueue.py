class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class QueueType:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self,e):
        n = Node(e)
        if self.isEmpty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.size += 1
    
    def dequeue(self):
        if not self.isEmpty():
            p = self.front
            data = p.data
            self.front = p.next
            self.size -= 1
            return data
        else:
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            pass
    
    def display(self):
        if self.isEmpty():
            print('No Elements')
            return
        p = self.front
        while p:
            print('[%s] -> '%p.data, end='')
            p = p.next
        print('\b\b\b   ')

if __name__ == '__main__':
    Q = QueueType()
    #print('[%s] is deleted'% (Q.dequeue()))
    Q.enqueue('A')
    Q.enqueue('B')
    Q.enqueue('C')
    Q.display()

    print('[%s] is deleted'% (Q.dequeue()))
    Q.display()

    print('peek : [%s]'% Q.peek())
    Q.display()