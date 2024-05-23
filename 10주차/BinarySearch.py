import random
from SelectionSort import selectionSort

def rBinarySearch(A, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print(A[mid],end=' ')
    if A[mid] == key:
        return mid
    elif key < A[mid]:
        return rBinarySearch(A, key, low, mid-1)
    else:
        return rBinarySearch(A, key, mid+1, high)

def iBinarySearch(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        print(A[mid],end=' ')
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

    
if __name__ == "__main__":
    A = []

    for i in range(15):
        A.append(random.randint(1, 100))
    
    selectionSort(A)
    print('A[] =',A)

    key = int(input('Input a key to search: '))
    print('rBS : %d'%rBinarySearch(A, key, 0, len(A)-1))
    print('iBS : %d'%iBinarySearch(A, key))
