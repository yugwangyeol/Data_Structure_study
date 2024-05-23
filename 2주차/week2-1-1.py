count = 0

def rFib(n):
    global count
    count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rFib(n-2) + rFib(n-1)

def iFib(n):
    if (n<2):
        return 0
    pp =0
    p =1
    for i in range(2,n+1):
        current = p+pp
        pp = p
        p = current
    
    return current

print('rfib : %d - count : %d'%(rFib(10),count))
print('ifib : %d '%(iFib(10)))