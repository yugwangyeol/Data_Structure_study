class ArrayStack:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isfull(self):
        return self.top == self.capacity - 1

    def push(self,e):
        if not self.isfull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('overflow')
    
    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('Empty!')
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty!')

    def sortedPush(self,e):
        if self.isEmpty() or self.peek() <= e:
            self.push(e) 
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)
    
    def display(self):
        print(self.stack[self.top::-1])

if __name__ == '__main__':
    stack = ArrayStack(10)

    data = [5,4,3,2,1,7,8,9]

    for i in data:
        stack.sortedPush(i)
        stack.display()
    