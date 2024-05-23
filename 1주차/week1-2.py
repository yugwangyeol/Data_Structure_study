def iFact(n):
    result =1 
    for i in range(n,0,-1):
        result = result*i
    return result

def rFact(n): 
    # 절대 반복문이 나오면 안 됨
    if n==1 :
        return 1
    else:
        return n*rFact(n-1)

print("iFact : %d"%iFact(5))
print("iFact : %d"%rFact(5))
print("rFact : %d , iFact : %d"%(rFact(5),iFact(5)))