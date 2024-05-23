import queue

Q = queue.Queue(maxsize=20)

for v in range(1,10):
    Q.put(v)
print("Queue :",end=' ')

for _ in range(1,10):
    print(Q.get(),end=' ')
print()

S = queue.LifoQueue(maxsize=20)

for v in range(1,10):
    S.put(v)
print("Stack :",end=' ')

for _ in range(1,10):
    print(S.get(),end=' ')
print()