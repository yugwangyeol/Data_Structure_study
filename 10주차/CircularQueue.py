class Node:
    def __init__(self, data, bext):
        self.data = data
        self.next = next

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.tail == None
    
    def enqueue(self,data):
        node = Node(data,None)

        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def display(self):
        if self.isEmpty():
            print('No Elements')
            return
        p = self.tail.next
        for i in range(self.size):
            print('[%s] -> '%p.data, end='')
            p = p.next
        print('\b\b\b   ')
    
    def dequeue(self):
        if not self.isEmpty():
            p = self.tail
            q = self.tail.next
            data = q.data
            if p==q:
                self.tail = None
            else:
                p.next = q.next
            self.size -= 1
            return data
        else:
            print('No Elements')

if __name__ == "__main__":
    Q = CircularQueue()
    
    Q.enqueue('A'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('C'); Q.display()

    print('[%s] is deleted'%Q.dequeue()); Q.display()

# 과제1 : Linked stack 만들기 (push,pop,peek,display) 단순 연결 리스트로 이용 
# 과제2 : 선형 Q 만들기 fornt 사용해서