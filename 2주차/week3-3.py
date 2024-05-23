L1 = [3,5,7,8]
L2 = ['A','B','C','D']

print(L1)
print('L1[0] :',L1[0])  

L2[2] = 'F'
print(L2)

L1.append(11)
print(L1)

print(L1.pop())
print(L1)

L2.extend(L1)
print(L2)
print(L1)

print(L2.count('B'))
L1.insert(2,4)
print(L1)