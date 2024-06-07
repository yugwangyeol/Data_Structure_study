class DListNode:
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next
        
class DListType:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
        
    def addFront(self,data):
        node = DListNode(data,None,self.front) #나의 다음 노드가 self.front 가 되어야 함 .. ?
        
        if self.size == 0:
            self.front = self.rear = node # 아무것도 없는 상황에서, 추가가 된다면 front 와 rear 가 새로 생성된 노드를 가르켜야 함 
        else:
            self.front.prev = node # 첫번째 노드의 prev 가 node 를 가르키게 하고 
            self.front = node # 그림 그려서 이해해보기 
        
        self.size += 1 
        
    def addRear(self,data):
        node = DListNode(data,self.rear,None) #주의! 구현시에 틀렸음! 
        
        if self.size == 0:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node 
            
        self.size += 1 
        
    def addPos(self,pos,data):
        node = DListNode(data,None,None) #일단은 미정 상태로 만들어 둠 
        
        if pos == 1:
            self.addFront(data)
        elif pos == self.size+1:
            self.addRear(data)
        else:
             p = self.front 
             for i in range(1,pos): #position 만큼 움직이기 , 범위 정하기! , 이중연결리스트의 장점. 어디서 멈추든 그냥 지정할 수 있음 
                 p = p.next
                 
            # 새로 생성된 노드가 누구를 카르켜야 하는지 먼저 정의 
             node.prev = p.prev
             node.next = p
            
            # 어떤 노드가 새롭게 생성된 노드를 가르켜야 하는지 정의 
             p.prev.next = node 
             p.prev = node 
             
    def deleteFront(self):
        if self.size == 0:
            print('There is no Node to delete')
        else:
            p = self.front
            data = p.data
            self.front = p.next
            
            if self.front == None: # 전체 리스트가 비어지는 상황을 표현 
                self.rear = None #예전 주소를 지우기 (비어지기 전의 주소)
            else:
                self.front.prev = None #새롭게 front 가 된 노드의 예전 주소 지우기 
            
            self.size -= 1 
            return data 
        
    def deleteRear(self):
        if self.size == 0:
            print('There is no Node to delete')
        else:
            p = self.rear
            data = p.data
            self.rear = p.prev
            
            if self.rear == None: # 전체 리스트가 비어지는 상황을 표현 
                self.front = None #예전 주소를 지우기 (비어지기 전의 주소)
            else:
                self.rear.next = None #새롭게 front 가 된 노드의 예전 주소 지우기 
            
            self.size -= 1 
            return data 
        
    def deletepos(self,pos):
        if self.size ==0:
            print('There is no Node to delete')
        elif self.pos == 1:
            self.deleteFront()
        elif self.pos == self.size+1:
            self.deleteRear()
        #else:
            
            
        
    def display(self):
        p = self.front
        
        while p != None:
            print('[%c] <-> '%p.data,end='')
            p = p.next
            
        # 맨 마지막 화살표 없애기 
        print('\b\b\b\b   ') # print 커서 뒤로 4번 back space 후 space 로 채우기 
        

if __name__ == '__main__':
    DL = DListType()
    
    DL.addFront('A');DL.addFront('B')
    DL.addRear('C');DL.addRear('D')
    DL.addPos(3,'E');DL.display()
    
    print('[%c]is deleted'%DL.deleteFront() , end='')
    DL.display()
    print('[%c]is deleted'%DL.deleteRear() , end='')
    DL.display()
    
    