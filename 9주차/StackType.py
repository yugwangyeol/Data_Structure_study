from ListNode import ListNode
from ListType import ListType

s = ListType()

def push(data):
    s.insertFirst(data)

def pop():
    return s.deleteFirst()

push('A'); s.display()
push('B'); s.display()
push('C'); s.display()

print('[%s] is popped' % pop()); s.display()