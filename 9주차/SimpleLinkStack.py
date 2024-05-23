class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def isEmpty(self):
        return self.top == None
    
    def push(self,e):
        n = Node(e,self.top)
        self.top = n
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            p = self.top
            data = p.data
            self.top = p.next
            self.size -= 1
            return data
        else:
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    
    def display(self):
        p = self.top
        while p != None:
            print('[%s] -> ' % p.data, end = '')
            p = p.next
        
        print('\b\b\b   ')

if __name__ == '__main__':
    S = StackType()
    #print('[%s] is deleted'% S.pop())
    S.push('A')
    S.push('B')
    S.push('C')
    S.display()

    print('[%s] is deleted'% S.pop())
    S.display()

    print('peek : [%s]'% S.peek())
    S.display()
