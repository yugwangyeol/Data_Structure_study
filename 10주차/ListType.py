from ListNode import ListNode

class ListType:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmtpy(self):
        return self.head == None
    
    def insertFirst(self,data):
        node = ListNode(data,self.head)
        self.head = node
        self.size += 1

    def getNode(self,pos):
        p = self.head

        for i in range(1,pos-1):
            p = p.next
        
        return p # position 이전 노드의 주소를 반환
    
    def insert(self,pos,data):
        if pos == 0:
            self.insertFirst(data)
        else:
            if (pos <= self.size):
                p = self.getNode(pos)
                node = ListNode(data,p.next)
                p.next = node
                self.size += 1
            else:
                print('Invalid position')
    
    def deleteFirst(self):
        if self.isEmtpy():
            print('No element')
        else:
            #self.head = self.head.next
            p = self.head
            self.head = p.next
            self.size -= 1
            return p.data
    
    def delete(self,pos):
        if self.isEmtpy():
            print('no element')
            return
        
        if pos == 1:
            return self.deleteFirst()
        else:
            if (pos <= self.size):
                q = self.getNode(pos)
                p = self.getNode(pos+1)
                q.next = p.next
                self.size -= 1
                return p.data
            else:
                print('Invalid position')
    
    def display(self):
        p = self.head
        while p != None:
            print('[%s] -> ' % p.data, end = '')
            p = p.next
        
        print('\b\b\b   ')
    
if __name__ == "__main__":
    L = ListType()

    L.insertFirst('A')
    L.insertFirst('B')
    L.display()

    L.insert(2,'C')
    L.insert(1,'D')
    L.display()

    L.insert(4,'E')
    L.insert(5,'F')
    L.display()

    print('[%s] is deleted'% L.deleteFirst())
    L.display()

    print('[%s] is deleted'% L.delete(5))
    L.display()

# 과제 delete first delete position
